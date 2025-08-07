from langchain_groq import ChatGroq
import os

def load_llm():
    # Initialize Groq's LLM with the API key from environment variable
    return ChatGroq(
        model="gemma2-9b-it",  # Or use "mixtral-8x7b-32768" for a smaller, faster model
        api_key='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',
        temperature=0.7,  # Adjust for randomness (0.0 = deterministic, 1.0 = more random)
        max_tokens=100,  # Limit response length
        max_retries=2  # Handle potential API timeouts
    )