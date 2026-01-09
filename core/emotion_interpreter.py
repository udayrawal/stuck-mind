# Responsibility: Infers transient emotional state from text; does not persist or label identity.


from typing import Literal 

class EmotionalInterpreter:
    """
    Infers lightweight emotional signals from text.
    Not a diagnosis. Not stored. Not asserted as fact.
    """

    def infer(self, text: str) -> str:
        t = text.lower()

        if any(k in t for k in ["exhausted", "tired", "no energy", "sleep"]):
            return "tired"

        if any(k in t for k in ["too much", "overwhelmed", "can't handle", "pressure"]):
            return "overwhelmed"

        if any(k in t for k in ["worried", "anxious", "scared", "stress"]):
            return "anxious"

        return "neutral"
