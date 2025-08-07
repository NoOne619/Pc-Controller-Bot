from langchain.memory import ConversationBufferMemory
import tiktoken

# Use tiktoken for token estimation (compatible with Groq models)
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")  # Approximation for gemma2-9b-it

MAX_TOKENS = 8192  # gemma2-9b-it context window
SAFE_TOKEN_LIMIT = int(MAX_TOKENS * 0.8)  # 6553 tokens

memory = ConversationBufferMemory(return_messages=True)

def get_memory():
    return memory

def should_use_memory():
    history = memory.buffer_as_messages
    all_text = ""
    for msg in history:
        all_text += f"{msg.type}: {msg.content}\n"
    
    tokens = len(tokenizer.encode(all_text))
    return tokens < SAFE_TOKEN_LIMIT