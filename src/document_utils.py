from PyPDF2 import PdfReader
import csv
from unstructured.partition.auto import partition
import streamlit as st
from text_processing import get_chunks, get_vectorstore
from conversation import get_conversationchain
from transformers import pipeline

# Import necessary libraries for summarization
import requests
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu
from bert_score import score as bert_score
import nltk
nltk.download('punkt')

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer YOUR_API_KEY_HERE"}  

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def summarize_text(text, min_length, max_length):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }
    output = query(payload)

    # Check if the API response is valid
    if isinstance(output, list) and len(output) > 0:
        return output[0]['summary_text']
    else:
        return "Error: Unable to get a summary."

# Summarizer model initialization
model_name = "sshleifer/distilbart-cnn-12-6"  
try:
    summarizer = pipeline("summarization", model=model_name)
except Exception as e:
    summarizer = None

def summarize(text, min_length=25, max_length=50):
    max_input_length = 1024  # Maximum input length for BART model

    # Truncate input text if necessary
    if len(text.split()) > max_input_length:
        text = ' '.join(text.split()[:max_input_length])
        st.warning("Input text was too long and has been truncated.")

    if summarizer is not None:
        try:
            summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            st.error("An error occurred during summarization.")
            return None
    else:
        return summarize_text(text, min_length, max_length)

def get_text_from_file(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)
            text = "".join(page.extract_text() for page in pdf_reader.pages)
            if not text.strip():
                raise ValueError("The PDF file is empty or couldn't be read properly.")
            return text
        
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode('utf-8')
            if not text.strip():
                raise ValueError("The text file is empty.")
            return text
        
        elif uploaded_file.type == "text/csv":
            text = "".join(", ".join(row) + "\n" for row in csv.reader(uploaded_file.read().decode('utf-8').splitlines()))
            if not text.strip():
                raise ValueError("The CSV file is empty or couldn't be read properly.")
            return text
        
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            elements = partition(file=uploaded_file)
            text = "\n".join(map(str, elements))
            if not text.strip():
                raise ValueError("The DOCX file is empty or couldn't be read properly.")
            return text
        
        else:
            st.error(f"Unsupported file type: {uploaded_file.type}")
            return None

    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
        return None

def get_text_from_docs(docs):
    separator = "\n\nnext docs: (previous information before this are from previous docs, ignore them)\n\n"
    text = ""
    for i, doc in enumerate(docs):
        file_text = get_text_from_file(doc)
        if file_text:
            if i > 0:
                text += separator  # Add separator before appending new document text
            text += file_text
    return text

def process_documents(docs):
    try:
        raw_text = get_text_from_docs(docs)
        text_chunks = get_chunks(raw_text)

        # Summarize each chunk
        summarized_chunks = [summarize(chunk) for chunk in text_chunks if chunk.strip()]

        # Use summarized chunks to create the vectorstore
        vectorstore = get_vectorstore(summarized_chunks)
        st.session_state.conversation = get_conversationchain(vectorstore)
        
        st.success("Documents have been processed successfully! You can now ask questions.")
    
    except Exception as e:
        st.error(f"An error occurred during document processing: {str(e)}")

