from memory_controller import MemoryController
from memory import Memory
from emotion_interpreter import EmotionalInterpreter
from response_guide import ResponseGuide
# PatternSuggester is optional for now
# from pattern_suggester import PatternSuggester


def chat_loop():
    print("Stuck Mind is here.")
    print("Say anything. Type 'exit' to stop.")

    memory = Memory()
    memory_controller = MemoryController(
        journal=memory,
        memory=memory,
        rules=None  # MemoryRules will be plugged in later
    )

    emotion_interpreter = EmotionalInterpreter()
    response_guide = ResponseGuide()
    # pattern_suggester = PatternSuggester()

    while True:
        user_input = input("> ").strip().lower()

        if user_input in ["exit", "quit", "i am done for today"]:
            print("I am here always for you. If you need anything.")
            break

        # 1. Memory routing (raw text only)
        memory_controller.process_input(user_input)

        # 2. Silent emotional inference (not stored)
        state = emotion_interpreter.infer(user_input)

        # 3. Optional pattern suggestion (future-safe)
        # pattern = pattern_suggester.suggest(memory.get_context()["recent_context"])

        # 4. Generate presence-only response
        response = response_guide.respond(
            state=state,
            context=memory.get_context()
        )

        print(response)

        # 5. Opt-in for long-term memory (if candidate exists)
        candidate = memory_controller.long_term_candidate
        if candidate:
            choice = input(
                "This feels familiar. Would you like me to remember this pattern? [y/n] "
            ).strip().lower()

            if choice == "y":
                memory.save_long(candidate)

            memory_controller.long_term_candidate = None


if __name__ == "__main__":
    chat_loop()
