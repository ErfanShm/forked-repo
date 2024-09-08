from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
import streamlit as st
from htmlTemplates import user_template, bot_template
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Prompts
prompt_search_query = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up to get information relevant to the conversation.")
])

prompt_get_answer = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
])

def get_conversationchain(vectorstore):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OPENAI_API_KEY not found in environment variables")
        return None

    try:
        llm = ChatOpenAI(temperature=0.2, base_url="https://api.avalai.ir/v1", api_key=openai_api_key)
        
        retriever = vectorstore.as_retriever()

        # Create history-aware retriever
        retriever_chain = create_history_aware_retriever(llm, retriever, prompt_search_query)

        # Create document chain
        document_chain = create_stuff_documents_chain(llm, prompt_get_answer)

        # Create retrieval chain
        retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

        return retrieval_chain
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None

def handle_question(question):
    if st.session_state.conversation:
        try:
            # Convert chat history to the format expected by the chain
            formatted_history = [
                (HumanMessage(content=msg["content"]) if msg["role"] == "user" else AIMessage(content=msg["content"]))
                for msg in st.session_state.chat_history
            ]

            # Prepare the input for the chain
            chain_input = {
                "chat_history": formatted_history,
                "input": question
            }

            # Invoke the chain
            response = st.session_state.conversation.invoke(chain_input)
            
            # Extract the answer from the response
            answer = response.get('answer', "I'm sorry, I couldn't generate an answer.")
            
            # Update chat history
            st.session_state.chat_history.append({"role": "user", "content": question})
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            
            # Display chat history
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.write(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error processing question: {str(e)}")
    else:
        st.error("Please process documents first before asking questions.")
