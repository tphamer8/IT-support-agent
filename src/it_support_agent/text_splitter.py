from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from it_support_agent.document_loader import load_support_docs


def split_support_docs(docs: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    return splitter.split_documents(docs)


def main() -> None:
    docs = load_support_docs()
    chunks = split_support_docs(docs)

    print(f"Loaded {len(docs)} documents")
    print(f"Created {len(chunks)} chunks")

    for chunk in chunks:
        print(f"- {chunk.metadata['source']}")


if __name__ == "__main__":
    main()
