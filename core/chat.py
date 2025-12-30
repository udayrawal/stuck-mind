def save_to_memory(user_input):
    pass


def chat():
    print("Stuck Mind is here.")
    print("Tell me what's going on.")

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("I'm here whenever you return.")
             
            break

        save_to_memory(user_input)

        print("I hear you.")
        print("We will handle this together.")
