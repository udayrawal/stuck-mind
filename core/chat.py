# Responsibility: Coordinates session flow and component interaction; contains no business logic.

from .memory_controller import MemoryController
from .memory import Memory
from .journal import Journal
from .memory_interface import MemoryInterface
from .emotion_interpreter import EmotionalInterpreter
from .response_guide import ResponseGuide
from .pattern_suggester import PatternSuggester
from .config import SAFE_FALLBACK_RESPONSE


def on_session_start():
    pass


def on_session_end(memory_controller):
    memory_controller.end_session()


def chat_loop():
    on_session_start()

    print("Stuck Mind is here.")
    print("Hi!, Uday go ahead, share whatever is on your mind.")

    # ---- instantiate core components ----

    journal = Journal()
    memory = Memory()
    rules = MemoryInterface()
    pattern_suggester = PatternSuggester()

    memory_controller = MemoryController(
        journal=journal,
        memory=memory,
        rules=rules,
        suggester=pattern_suggester
    )

    emotion_interpreter = EmotionalInterpreter()
    response_guide = ResponseGuide()

    while True:
        raw_input = input("> ").strip()

        if raw_input.lower() == "bye":
            on_session_end(memory_controller)
            print("I am here always for you. If you need anything.")
            break

        # Memory routing (must always run)
        memory_controller.process_input(raw_input)

        try:
            state = emotion_interpreter.infer(raw_input)

            response = response_guide.respond(
                state=state,
                context=memory.get_context()
            )

            print(response)

        except Exception:
            print(SAFE_FALLBACK_RESPONSE)

        # Opt-in for long-term memory (if candidate exists)
        candidate = memory_controller.long_term_candidate
        if candidate:
            print(response_guide.familiarity_line())
            choice = input(
                "This feels familiar. Would you like me to remember this pattern? [y/n] "
            ).strip().lower()

            if choice == "y":
                memory.save_long(candidate)

            memory_controller.long_term_candidate = None


if __name__ == "__main__":
    chat_loop()
