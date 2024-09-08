import streamlit as st
from document_utils import process_documents
from conversation import handle_question, user_template, bot_template
from htmlTemplates import css
import nltk
from nltk.corpus import wordnet as wn
import spacy

nlp = spacy.load('en_core_web_sm')

def simplify_language(text):
    """Simplify the language by replacing complex words with simpler synonyms."""
    words = nltk.word_tokenize(text)
    simplified_words = []
    for word in words:
        synonyms = wn.synsets(word)
        if synonyms:
            # Get the simplest synonym based on word length
            simple_word = min((syn.name().split('.')[0] for syn in synonyms), key=len)
            simplified_words.append(simple_word)
        else:
            simplified_words.append(word)
    return ' '.join(simplified_words)

def add_context(text):
    """Add additional context if necessary. For example, if the text is vague, append some default context."""
    # Here we check if the text is too short or lacks certain keywords, and add context if needed
    if len(text.split()) < 5:  # Example condition for adding context
        text += " Please provide more details."
    return text

def rephrase_prompt(text):
    """Rephrase the text for clarity using basic NLP techniques."""
    doc = nlp(text)
    sentences = list(doc.sents)
    rephrased_sentences = []
    
    for sentence in sentences:
        words = [token.text for token in sentence]
        # Reorder the sentence for clarity, e.g., by moving the subject to the front
        # This is a simple example and may be adjusted for more complex logic
        if len(words) > 1:
            rephrased_sentence = ' '.join(sorted(words, key=lambda x: nlp(x).vector_norm, reverse=True))
            rephrased_sentences.append(rephrased_sentence)
        else:
            rephrased_sentences.append(' '.join(words))
    
    return ' '.join(rephrased_sentences)

def refine_prompt(prompt):
    refined_prompt = prompt.strip()
    refined_prompt = simplify_language(refined_prompt)
    refined_prompt = add_context(refined_prompt)
    refined_prompt = rephrase_prompt(refined_prompt)
    refined_prompt = f"Refined Prompt: {refined_prompt}"
    return refined_prompt

def main():
    st.set_page_config(page_title="Chat with Multiple Documents", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    # Initialize session state variables
    if "docs" not in st.session_state:
        st.session_state.docs = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processed" not in st.session_state:
        st.session_state.processed = False

    st.header("Chat with Your Documents :books:")

    # Sidebar
    with st.sidebar:
        st.markdown("## :information_source: About")
        st.info("**Upload your files and press 'Process'** to prepare the documents for questioning.")

        with st.expander("Need Help?"):
            st.write("""
                - **Upload files**: Use the file uploader to upload your documents.
                - **Supported formats**: PDF, TXT, CSV, DOCX.
                - **Process files**: Click 'Process' to analyze the uploaded documents.
            """)

        # Document uploader
        docs = st.file_uploader("Upload your files here", accept_multiple_files=True, type=["pdf", "txt", "csv", "docx"])
        if docs:
            st.session_state.docs = docs
            st.subheader("Uploaded Files")
            for i, doc in enumerate(docs):
                st.write(f"{i+1}. {doc.name}")

        # Processing logic
        if st.button("Process"):
            if docs:
                with st.spinner("Processing documents, please wait..."):
                    st.session_state.chat_history = []
                    st.session_state.conversation = None
                    process_documents(docs)
                    st.session_state.processed = True
            else:
                st.error("Please upload at least one document before processing.")

    # Main chat area
    chat_container = st.container()

    # Status message
    if st.session_state.processed:
        st.success("Documents have been processed successfully! You can now ask questions.")

    # Text input for asking questions
    with st.form(key="question_form"):
        question = st.text_input("Ask a question from your document:")
        submit_button = st.form_submit_button("Submit")

    if submit_button and question:
        # Refine the prompt before sending it to the model
        refined_question = refine_prompt(question)
        handle_question(refined_question)

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()  # Rerun the app to apply the changes

if __name__ == '__main__':
    main()
