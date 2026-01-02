from memory_controller import MemoryController
from memory import Memory

def chat_loop():
    print("Stuck Mind is here.")
    print("Say anything. Type 'exit' to stop.")

    memory = Memory()
    memory_controller = MemoryController(
        journal=memory,
        memory=memory,
        rules=None  # placeholder for now
    )

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("I'm here whenever you return.")
            break

        memory_controller.process_input(user_input)

        context = memory.get_context()

        print("I hear you.")

if __name__ == "__main__":
    chat_loop()
