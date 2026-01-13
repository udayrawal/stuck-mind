# Responsibility: Generates safe, presence-first responses; 
# contains no advice or memory logic.

from .config import ABSOLUTE_WORDS, IMPERATIVE_WORDS, SAFE_FALLBACK_RESPONSE


class ResponseGuide:

    def respond(self, state: str, context: dict) -> str:
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

        elif state == "Unknown":
            response = "We can stay with this for a moment."

        else:
            response = "I’m listening."

        if not self._is_safe(response):
            return SAFE_FALLBACK_RESPONSE

        return response

    def familiarity(self) -> str:
        response = "This feels familiar."
        if not self._is_safe(response):
            return SAFE_FALLBACK_RESPONSE
        return response


    def _is_safe(self, text: str) -> bool:
        lower = text.lower()

        if any(word in lower for word in ABSOLUTE_WORDS):
            return False

        if any(word in lower for word in IMPERATIVE_WORDS):
            return False

        return True
