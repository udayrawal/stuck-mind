from memory import save_entry


def chat_loop():
    print("Stuck Mind is here.")
    print("Say anything. Type 'exit' to stop.")

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("I'm here whenever you return.")
            break

        save_entry(user_input)

        print("I hear you.")


if __name__ == "__main__":
    chat_loop()