class ResponseGuide:
    """
    Produces presence-first responses.
    Guards against advice, absolutes, and imperatives.
    """

    FORBIDDEN_WORDS = [
        "always",
        "never",
        "should",
        "try",
        "do this",
        "must",
        "next step"
    ]

    def respond(self, state: str, context: dict) -> str:
        if state == "tired":
            response = "I hear how drained this feels."

        elif state == "overwhelmed":
            response = "That sounds like a lot to carry."

        elif state == "anxious":
            response = "I’m here with this."

        else:
            response = "I’m listening."

        # Guard clause: fallback if unsafe language detected
        if not self._is_safe(response):
            return "I’m here. We can continue, or pause."

        return response

    def _is_safe(self, text: str) -> bool:
        lower = text.lower()
        return not any(word in lower for word in self.FORBIDDEN_WORDS)
