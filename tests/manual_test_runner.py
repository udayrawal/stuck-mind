# tests/manual_test_runner.py

from core.memory import Memory
from core.journal import Journal
from core.memory_interface import MemoryInterface
from core.memory_controller import MemoryController
from core.emotion_interpreter import EmotionalInterpreter
from core.pattern_suggester import PatternSuggester
from core.response_guide import ResponseGuide


def run_case(name, inputs):
    print(f"\n--- {name.upper()} ---")

    # Initialize fresh session
    journal = Journal()
    memory = Memory()
    rules = MemoryInterface()
    suggester = PatternSuggester()

    controller = MemoryController(
        journal=journal,
        memory=memory,
        rules=rules,
        suggester=suggester
    )

    interpreter = EmotionalInterpreter()
    guide = ResponseGuide()

    for text in inputs:
        print(f"\n> {text}")

        try:
            controller.process_input(text)
            state = interpreter.infer(text)
            context = memory.get_context()
            response = guide.respond(state, context)
            print(response)

        except Exception:
            print("I’m here. We can take this slowly.")

    # Explicit session end
    controller.end_session()
    print("\n[session ended]")


if __name__ == "__main__":
    # Baseline
    run_case(
        "baseline",
        ["I feel tired", "I keep avoiding starting"]
    )

    # Neutral statements
    run_case(
        "neutral",
        ["Just a normal day", "Nothing special"]
    )

    # Identity statement
    run_case(
        "identity",
        ["I am broken"]
    )

    # Private marker
    run_case(
        "private",
        ["[private] this should not be stored"]
    )

    # Repetition
    run_case(
        "repetition",
        ["I feel stuck", "I feel stuck", "I feel stuck"]
    )

    # Opt-in refusal (simulate by ignoring candidate manually)
    run_case(
        "opt_in_refusal",
        ["I keep doing the same thing again and again"]
    )

    # Session reset check
    run_case(
        "session_reset",
        ["First session thought"]
    )
    run_case(
        "session_reset_followup",
        ["Second session thought"]
    )
    