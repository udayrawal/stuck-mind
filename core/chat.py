from core.memory import save_thought

def chat():
    print("Stuck Mind is here.")
    print("Tell me what's going on.")

    user_input = input("> ")   
    
    save_thought(user_input)

    print("\nI hear you.")
    print("We will handle this together.")

if __name__ == "__main__":
    chat()
