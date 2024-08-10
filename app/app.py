import streamlit as st
from document_utils import process_documents
from conversation import handle_question
from htmlTemplates import css

def main():
    st.set_page_config(page_title="Chat with multiple Documents", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "docs" not in st.session_state:
        st.session_state.docs = []

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple Documents :books:")

    if st.button("Clear Chat History"):
        st.session_state.chat_history = None
        if st.session_state.conversation:
            st.session_state.conversation.memory.clear()
        st.experimental_rerun()

    question = st.text_input("Ask a question from your document:")
    if question:
        handle_question(question)
        
    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader("Upload your files here and click on 'Process'", 
                                accept_multiple_files=True, 
                                type=["pdf", "txt", "csv", "docx"])

        if docs:
            st.session_state.docs = docs

            st.subheader("Uploaded Files")
            for i, doc in enumerate(st.session_state.docs):
                st.write(f"{i+1}. {doc.name}")

        if st.button("Process"):
            if st.session_state.docs:
                with st.spinner("Processing"):
                    st.session_state.chat_history = None
                    st.session_state.conversation = None
                    process_documents(st.session_state.docs)
            else:
                st.error("Please upload at least one document before processing.")

if __name__ == '__main__':
    main()
