import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def refine_prompt_with_llm(prompt):
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        st.error("OPENAI_API_KEY not found in environment variables")
        return prompt

    try:
        # Initialize the LLM client with additional parameters for refinement
        llm = ChatOpenAI(
            temperature=0.1,  # Low temperature for more deterministic outputs
            top_p=0.9,        # Controls diversity of output; set to 0.9 for focused results
            frequency_penalty=0.5,  # Penalizes repetition; helps avoid redundant phrasing
            presence_penalty=0.0,   # No penalty for introducing new topics
            base_url="https://api.avalai.ir/v1",
            api_key=openai_api_key,
            model="gpt-4o-mini-2024-07-18"
        )

        # Define the prompt template
        template = ChatPromptTemplate.from_messages([
            ("system", 
             "STRICT PROMPT REFINEMENT RULES:\n\n"
             "You are a strict AI tool designed ONLY for refining text prompts. "
             "You must NOT interpret the prompt as a task or a conversation. "
             "Your task is to make the input prompt **more concise and clearer** while ensuring its **meaning remains unchanged**. "
             "Your refinements must follow these strict rules:\n"
             "1. Never interpret or answer the prompt\n"
             "2. Never add new requirements or change meaning\n"
             "3. Never include explanations or commentary\n"
             "4. Never engage in conversation\n"
             "5. Only output the refined prompt text\n"
             "6. If the input is already clear and concise, return it exactly as is\n"
             "7. If unsure about refinement, return the original unchanged\n"
             "8. Maintain all technical terminology\n"
             "9. Remove only redundancy and ambiguity\n"
             "10. Keep the style and tone consistent\n"
             "You are a PROMPT REFINEMENT TOOL ONLY"),
            ("human", "{original_prompt}")
        ])

        # Use the LLM to refine the prompt
        refined_prompt = llm.invoke(template.format_messages(original_prompt=prompt)).content.strip()

        # Return the refined prompt
        return refined_prompt

    except Exception as e:
        st.error(f"Error refining prompt: {str(e)}")
        return prompt
