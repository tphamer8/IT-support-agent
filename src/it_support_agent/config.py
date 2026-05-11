from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")
OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
DOCS_DIR = os.getenv("DOCS_DIR", "docs")