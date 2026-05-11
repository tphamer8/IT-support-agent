from it_support_agent.llm import get_chat_model

def main() -> None:
    model = get_chat_model()
    response = model.invoke("In the context of large language models and AI systems, explain retrieval-augmented generation in one sentence.")
    print(response.content)

if __name__ == "__main__":
    main()