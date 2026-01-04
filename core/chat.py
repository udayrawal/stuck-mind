from memory_controller import MemoryController
from memory import Memory
from emotion_interpreter import EmotionalInterpreter


RESPONSES = {
    "tired": "I hear how drained this feels.",
    "overwhelmed": "That sounds like a lot to carry right now.",
    "anxious": "It makes sense that this feels uneasy.",
    "neutral": "I’m here. Go on."
}


def chat_loop():
    print("Stuck Mind is here.")
    print("Say anything. Type 'exit' to stop.")

    memory = Memory()
    memory_controller = MemoryController(
        journal=memory,
        memory=memory,
        rules=None  # placeholder for now
    )

    emotion_interpreter = EmotionalInterpreter()

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("I'm here whenever you return.")
            break

        # 1. Silent emotional inference
        state = emotion_interpreter.infer(user_input)

        # 2. Memory routing
        memory_controller.process_input(user_input)

        # 3. Presence-only response
        response = RESPONSES.get(state, RESPONSES["neutral"])
        print(response)

        # 4. Opt-in prompt for long-term memory (NEW)
        candidate = memory_controller.long_term_candidate
        if candidate:
            choice = input(
                "This feels familiar. Would you like me to remember this pattern? [y/n] "
            ).strip().lower()

            if choice == "y":
                memory.save_long(candidate)

            # Clear candidate either way (no pressure, no repeat)
            memory_controller.long_term_candidate = None


if __name__ == "__main__":
    chat_loop()
