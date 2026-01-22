# Responsibility:
# Coordinates session flow and component interaction.
# Contains NO business logic.

from .memory_controller import MemoryController
from .memory import Memory
from .journal import Journal
from .brain import Brain
from .memory_interface import MemoryInterface
from .emotion_interpreter import EmotionalInterpreter
from .response_guide import ResponseGuide
from .pattern_suggester import PatternSuggester
from .config import SAFE_FALLBACK_RESPONSE, ENABLE_AUDIO


def on_session_start():
    pass


def on_session_end(memory_controller):
    memory_controller.end_session()


def chat_loop():
    on_session_start()

    print("Stuck Mind is here.")
    print("Hi!, Uday go ahead, share whatever is on your mind.")

    # ---- core components ----
    journal = Journal()
    memory = Memory()
    rules = MemoryInterface()
    brain = Brain()
    pattern_suggester = PatternSuggester()

    memory_controller = MemoryController(
        journal=journal,
        memory=memory,
        rules=rules,
        suggester=pattern_suggester
    )

    emotion_interpreter = EmotionalInterpreter()
    response_guide = ResponseGuide()

    # ---- optional audio (lazy init) ----
    speaker = None
    if ENABLE_AUDIO:
        from .audio.local_tts import LocalTTSSpeaker
        speaker = LocalTTSSpeaker()

    while True:
        raw_input = input("> ").strip()

        if not raw_input:
            continue

        if raw_input.lower() == "bye":
            on_session_end(memory_controller)
            print("I am here always for you. If you need anything.")
            break

        # 1. Memory routing (always runs)
        memory_controller.process_input(raw_input)

        # 2. Decide tone + respond
        try:
            state = emotion_interpreter.infer(raw_input)
            tone = brain.decide(state, memory.get_context())

            response = response_guide.respond(
                text=raw_input,
                tone=tone
            )
            print(response)

            if speaker:
                speaker.speak(response, tone=tone)

        except Exception:
            print(SAFE_FALLBACK_RESPONSE)
            continue

        # 3. Familiarity flow (response-only + consent)
        candidate = memory_controller.long_term_candidate

        if candidate:
            print(response_guide.familiarity_message())

            choice = input(
                "Would you like me to remember this pattern? [y/n] "
            ).strip().lower()

            if choice == "y":
                memory.save_long(candidate["text"])

            memory_controller.long_term_candidate = None


if __name__ == "__main__":
    chat_loop()
