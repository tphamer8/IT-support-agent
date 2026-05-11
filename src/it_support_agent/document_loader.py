from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document
from it_support_agent.config import DOCS_DIR

def load_support_docs() -> list[Document]:
    loader = DirectoryLoader(
        path=DOCS_DIR,
        glob="**/*.md", # Find all files ending in .md in this folder and any subfolders
        loader_cls=TextLoader,
    )
    return loader.load() # reads file and returns loaded data

if __name__ == "__main__":
    documents = load_support_docs()
    print(f"Loaded {len(documents)} documents")
    for document in documents:
        print(f"- {document.metadata['source']}")