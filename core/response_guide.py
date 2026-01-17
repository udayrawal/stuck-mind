# Responsibility: Generates safe, presence-first responses;
# contains no advice, memory logic, or decision-making.

from .config import ABSOLUTE_WORDS, IMPERATIVE_WORDS, SAFE_FALLBACK_RESPONSE


class ResponseGuide:
    """
    Produces presence-first responses based on transient emotional state.
    Does NOT give advice.
    Does NOT store or access memory.
    """

    def respond(self, state: str, context: dict) -> str:
        """
        Generate a safe, non-directive response.

        `context` is intentionally unused for now.
        It exists for future expansion (tone modulation, reflection).
        """

        if state == "tired":
            response = "I hear how drained this feels."

        elif state == "overwhelmed":
            response = "That sounds like a lot to carry."

        elif state == "anxious":
            response = "I’m here with this."

        elif state == "avoidant":
            response = "It sounds like you’re pulling away a bit."

        elif state == "confused":
            response = "It feels unclear right now."

        elif state == "sad":
            response = "I’m with you in this sadness."

        elif state == "neutral":
            response = "I’m here with you."

        else:
            response = "I’m listening."

        return response if self._is_safe(response) else SAFE_FALLBACK_RESPONSE

    def familiarity_message(self) -> str:
        """
        Response-only familiarity signal.
        NO consent logic here.
        NO memory access here.
        """
        message = "This feels familiar."
        return message if self._is_safe(message) else SAFE_FALLBACK_RESPONSE

    def _is_safe(self, text: str) -> bool:
        """
        Guards against absolute or imperative language.
        """
        lower = text.lower()

        if any(word in lower for word in ABSOLUTE_WORDS):
            return False

        if any(word in lower for word in IMPERATIVE_WORDS):
            return False

        return True
