class ResponseGuide:
    """
    Produces presence-first responses.
    Listens more than it speaks.
    Never asks meta-questions.
    """

    def respond(self, state: str, context: dict) -> str:
        if state == "tired":
            return "I hear how drained this feels."

        if state == "overwhelmed":
            return "That sounds like a lot to carry."

        if state == "anxious":
            return "I’m here with this."

        return "I’m listening."
