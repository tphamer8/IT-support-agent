from it_support_agent.classifier import IntentClassifier

def main() -> None:
    print("IT Support Agent")
    print("Type 'exit' or 'quit' to end the session")


    while True:
        user_input = input("\nUser: ").strip()

        # Exit conditions
        if user_input.lower() in {'exit', 'quit'}:
            print("Agent: Goodbye.")
            break

        # No message condition
        if not user_input:
            print("Agent: Please enter a support question.")
            continue

        # Find intent
        classifier = IntentClassifier()
        user_intent = IntentClassifier.classify(classifier, user_input)

        print("Agent: I received your question. Intent:", user_intent)

if __name__ == "__main__":
    main()