# Document Chatbot with Retrieval Augmented Generation (RAG)

Welcome to the Document Chatbot with Retrieval Augmented Generation (RAG) repository! This guide provides a comprehensive overview of how to deploy a chatbot that enhances document information retrieval using advanced AI techniques. The project demonstrates the integration of the RAG methodology with an intuitive Streamlit interface, enabling efficient and interactive querying of various document types.

## Table of Contents
- [Overview](#overview)
- [Retrieval Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
- [Project Features](#project-features)
- [Prerequisites](#prerequisites)
- [Installation Instructions](#installation-instructions)
- [Contributing](#contributing)
- [Additional Resources](#additional-resources)
- [License](#license)

## Overview

This project aims to create a user-centric and intelligent system that enhances information retrieval from documents through natural language queries. The focus is on streamlining the user experience by developing an intuitive interface that allows users to interact with document content effortlessly. The Retrieval Augmented Generation (RAG) methodology introduced by Meta AI researchers is employed to achieve this, combining the strengths of retrieval-based and generative AI models.

https://github.com/user-attachments/assets/b6066983-d1d1-45b4-b652-ca7e745e72c9

## Retrieval Augmented Generation (RAG)

### Introduction

RAG addresses knowledge-intensive tasks by combining an information retrieval component with a text generation model, enabling adaptive and efficient knowledge processing. Unlike traditional methods requiring extensive retraining for updates, RAG allows for fine-tuning internal knowledge with minimal effort.

### Workflow

1. **Input**: Multiple documents are ingested as input.
2. **VectorStore**: Documents are converted into a vector store using FAISS and OpenAI embeddings (1024 dimensions).
3. **Memory**: A conversation buffer memory tracks previous interactions, feeding them to the LLM model alongside the user query.
4. **Text Generation with GPT-3.5 Turbo**: The processed input is sent to the GPT-3.5 Turbo model via the OpenAI API, generating the final output.
5. **User Interface**: Streamlit powers the user-friendly interface.

### Benefits

- **Adaptability**: Suited for dynamic knowledge domains where facts may evolve.
- **Efficiency**: Provides access to the latest information without extensive retraining.
- **Reliability**: Ensures accurate outputs by leveraging both retrieval-based and generative approaches.

## Project Features

1. **User-friendly Interface**: Intuitive interface for handling natural language queries across various document types.
2. **Seamless Navigation**: Streamlined information retrieval enhances user experience and reduces complexity.
3. **Support for Multiple Document Types**: Retrieve and analyze information from PDFs, TXT files, CSV files, and DOCX files.
4. **Chat History**: Each chat maintains its history, allowing the bot to remember previous conversations unless you clear the history.

## Prerequisites

Before getting started, ensure you have the following tools installed:

- **uv**: Install via pip:

   ```bash
   pip install uv
   ```

   For more details, visit the [uv documentation page](https://pypi.org/project/uv/).

- **Python-dotenv**: Manage environment variables easily. Install it via pip with:

    ```bash
    pip install python-dotenv
    ```

    You will need to create a `.env` file in the root directory of the project and add your OpenAI API key in the following format:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Without this key, the application will not be able to access the OpenAI API for GPT-3.5 Turbo and embedding models.

- **OpenAI API Key**: Ensure you have an API key from OpenAI. This key is essential for interacting with GPT-3.5 Turbo and embedding models. Add it to your `.env` file as described above.

- **Bash**: Included with Unix-based systems (Linux, macOS). Windows users can use Git Bash or Windows Subsystem for Linux (WSL).

## Installation Instructions

Follow these steps to set up your environment and install the necessary packages:

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ErfanShm/ChatDoc.git
   cd ChatDoc
   ```

2. **Run the Setup Script**

   The `setup.sh` script automates the environment setup, including virtual environment creation, dependency synchronization, and application launch options:

   ```bash
   bash setup.sh
   ```

   Choose from the following options:
   - Sync dependencies
   - Run with Streamlit interface
   - Exit

3. **Access the User Interface**

   Once running, access the user interface by navigating to `http://localhost:8000` in your browser (usually done automatically).

## Contributing

Contributions are welcome! If you have suggestions, improvements, or additional features, feel free to open an issue or create a pull request. Let's work together to enhance this tool's utility.

## Additional Resources

Enhance your understanding of Retrieval Augmented Generation (RAG), document analysis, and related technologies with these resources:

- [Meta AI's RAG Paper](https://arxiv.org/abs/2005.11401)
- [Understanding Retrieval-Augmented Generation](https://huggingface.co/blog/rag)
- [Working with PDFs in Python](https://realpython.com/pdf-python/)
- [Text Extraction from Documents](https://towardsdatascience.com/text-extraction-from-documents-with-python-47a277b7b7e1)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Tutorials](https://streamlit.io/learn)
- [FAISS: A Library for Efficient Similarity Search](https://faiss.ai/)
- [Vector Search with FAISS](https://towardsdatascience.com/vector-search-with-faiss-b3e1dfd34f6c)
- [Unstructured IO GitHub Repository](https://github.com/Unstructured-IO/unstructured)
- [LangChain PDF Document Loader](https://python.langchain.com/v0.2/docs/how_to/document_loader_pdf/)
- [LangChain Office File Document Loader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/office_file/)
- [LangChain CSV Document Loader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/csv/)
- [LangChain Retrieval Chain API Documentation](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval.create_retrieval_chain.html)
- [LangChain History-Aware Retriever API Documentation](https://api.python.langchain.com/en/latest/chains/langchain.chains.history_aware_retriever.create_history_aware_retriever.html)
- [LangChain Stuff Documents Chain API Documentation](https://api.python.langchain.com/en/latest/chains/langchain.chains.combine_documents.stuff.create_stuff_documents_chain.html)
- [Beginner's Guide to Conversational Retrieval Chain Using LangChain](https://vijaykumarkartha.medium.com/beginners-guide-to-conversational-retrieval-chain-using-langchain-3ddf1357f371)
- [Streamlit Warning API Reference](https://docs.streamlit.io/develop/api-reference/status/st.warning)
- [Streamlit LLM Examples on GitHub](https://github.com/streamlit/llm-examples/tree/main/pages)
- [ChatPDF Repository on GitHub](https://github.com/ArmaanSeth/ChatPDF/tree/main?tab=readme-ov-file)

## License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code, provided you include the original copyright notice and license.
