# Document Chatbot with Retrieval Augmented Generation (RAG)

Welcome to the Document Chatbot with Retrieval Augmented Generation (RAG) repository! This guide provides a comprehensive overview of how to deploy a chatbot that enhances document information retrieval using advanced AI techniques. The project demonstrates the integration of the RAG methodology with an intuitive Streamlit interface to enable efficient and interactive querying of various document types.

- **Project Files:** This repository contains the scripts and resources necessary to deploy the Document Chatbot using Retrieval Augmented Generation (RAG). It includes code for handling document processing, vector storage with FAISS, and interaction through a Streamlit interface.

## Overview

The goal of this project is to create a user-centric and intelligent system that enhances information retrieval from PDF documents through natural language queries. The project focuses on streamlining the user experience by developing an intuitive interface, allowing users to interact with PDF content using language they are comfortable with. To achieve this, we leverage the Retrieval Augmented Generation (RAG) methodology introduced by Meta AI researchers.


https://github.com/ArmaanSeth/ChatPDF/assets/99117431/2500f636-c66d-46ad-bb68-1d55f04ce753


## Retrieval Augmented Generation (RAG)

### Introduction

RAG is a method designed to address knowledge-intensive tasks, particularly in information retrieval. It combines an information retrieval component with a text generator model to achieve adaptive and efficient knowledge processing. Unlike traditional methods that require retraining the entire model for knowledge updates, RAG allows for fine-tuning and modification of internal knowledge without extensive retraining.

### Workflow

1. **Input**: RAG takes multiple pdf as input.
2. **VectoreStore**: The pdf's are then converted to vectorstore using FAISS and all-MiniLM-L6-v2 Embeddings model from Hugging Face.
3. **Memory**: Conversation buffer memory is used to maintain a track of previous conversation which are fed to the llm model along with the user query.
4. **Text Generation with GPT-3.5 Turbo**: The embedded input is fed to the GPT-3.5 Turbo model from the OpenAI API, which produces the final output.
5. **User Interface**: Streamlit is used to create the interface for the application.

### Benefits

- **Adaptability**: RAG adapts to situations where facts may evolve over time, making it suitable for dynamic knowledge domains.
- **Efficiency**: By combining retrieval and generation, RAG provides access to the latest information without the need for extensive model retraining.
- **Reliability**: The methodology ensures reliable outputs by leveraging both retrieval-based and generative approaches.

## Project Features

1. **User-friendly Interface**: An intuitive interface designed to handle natural language queries, simplifying interaction with various document types.

2. **Seamless Navigation**: Streamlined information retrieval enhances user experience and reduces complexity.

3. **Support for Multiple Document Types**: Analyze and retrieve information from PDFs, TXT files, CSV files, and DOCX files.

## Getting Started

To use the PDF Intelligence System:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/ArmaanSeth/ChatPDF.git
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Application

   After setting up the environment, you can start the application by pressing `1` when prompted by the `setup_environment.sh` script. Alternatively, you can manually run the application using the following command:

   ```bash
   streamlit run app.py
   ```

   Then, open your browser and navigate to `http://localhost:8000` to access the user interface.


## Contributing

Contributions to enhance this application are welcome! If you have suggestions, improvements, or additional features, please feel free to open an issue or create a pull request. Let's collaborate to make this tool even more useful.

## Additional Resources

Explore these resources to enhance your understanding of Retrieval Augmented Generation (RAG), document analysis, and related technologies:

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
- [ChatPDF Repository on GitHub](https://github.com/ArmaanSeth/ChatPDF/tree/main?tab=readme-ov-file)
- [LangChain CSV Document Loader](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/csv/)

## License

The content in this repository is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code, provided you include the original copyright notice and license.

## Acknowledgments

We would like to express our gratitude to the following communities and organizations:

- [Hugging Face](https://huggingface.co/) - For providing the all-MiniLM-L6-v2 Embeddings model.
- [OpenAI](https://openai.com/) - For providing the GPT-3.5 Turbo model through their API.
- [LangChain](https://python.langchain.com/) - For their tools and libraries used in document loading and processing.
- [Streamlit](https://streamlit.io/) - For the powerful framework used to build the interactive user interface.

