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

        print("Agent: I received your question. Intent routing will be added next.")

if __name__ == "__main__":
    main()