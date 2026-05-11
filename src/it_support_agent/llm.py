from it_support_agent.config import OLLAMA_CHAT_MODEL
from langchain_ollama import ChatOllama

def get_chat_model() -> ChatOllama:
    return ChatOllama(
        model=OLLAMA_CHAT_MODEL, # uses config.py value, currently llama3.2
        temperature=0, # more consistent/deterministic answers
    )


