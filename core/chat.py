from memory_controller import MemoryController
from memory import Memory
from emotion_interpreter import EmotionalInterpreter
from response_guide import ResponseGuide


def on_session_start():
    """
    Called when a chat session starts.
    """
    pass


def on_session_end(memory_controller):
    """
    Called when a chat session ends.
    Clears short-term memory only.
    """
    memory_controller.end_session()


def chat_loop():
    on_session_start()

    print("Stuck Mind is here.")
    print("Hi!, Uday go ahead, share whatever is on your mind.")

    memory = Memory()
    memory_controller = MemoryController(
        journal=memory,
        memory=memory,
        rules=None
    )

    emotion_interpreter = EmotionalInterpreter()
    response_guide = ResponseGuide()

    while True:
        raw_input = input("> ")
        user_input = raw_input.strip().lower()

        if user_input in ["bye"]:
            on_session_end(memory_controller)
            print("I am here always for you. If you need anything.")
            break

        # Memory routing (must always run)
        memory_controller.process_input(raw_input)

        try:
            # Interpreter
            state = emotion_interpreter.infer(raw_input)

            # Guide
            response = response_guide.respond(
                state=state,
                context=memory.get_context()
            )

            print(response)

        except Exception:
            # Safety fallback — presence only
            print("I’m here. We can take this slowly.")

        # Opt-in for long-term memory (if candidate exists)
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
