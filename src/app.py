import streamlit as st
from document_utils import process_documents
from conversation import handle_question,user_template,bot_template
from htmlTemplates import css

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
        handle_question(question)

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()  # Rerun the app to apply the changes

if __name__ == '__main__':
    main()