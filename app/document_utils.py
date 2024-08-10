from PyPDF2 import PdfReader
import csv
from unstructured.partition.auto import partition
import streamlit as st
from text_processing import get_chunks, get_vectorstore
from conversation import get_conversationchain

def get_text_from_file(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            if not text.strip():
                raise ValueError("The PDF file is empty or couldn't be read properly.")
            return text
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode('utf-8')
            if not text.strip():
                raise ValueError("The text file is empty.")
            return text
        elif uploaded_file.type == "text/csv":
            text = ""
            csv_reader = csv.reader(uploaded_file.read().decode('utf-8').splitlines())
            for row in csv_reader:
                text += ", ".join(row) + "\n"
            if not text.strip():
                raise ValueError("The CSV file is empty or couldn't be read properly.")
            return text
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            elements = partition(file=uploaded_file)
            text = "\n".join([str(el) for el in elements])
            if not text.strip():
                raise ValueError("The DOCX file is empty or couldn't be read properly.")
            return text
        else:
            st.error("Unsupported file type.")
            return None
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
        return None

def get_text_from_docs(docs):
    text = ""
    for doc in docs:
        file_text = get_text_from_file(doc)
        if file_text:
            text += file_text + "\n\n"
    return text

def process_documents(docs):
    try:
        raw_text = get_text_from_docs(docs)
        text_chunks = get_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks)
        st.session_state.conversation = get_conversationchain(vectorstore)
        
        st.success("Documents have been processed successfully! You can now ask questions.")
    
    except Exception as e:
        st.error(f"An error occurred during document processing: {str(e)}")
