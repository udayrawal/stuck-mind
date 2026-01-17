# Responsibility: Determines response intent from emotion and context.
# Does NOT speak.
# Does NOT store memory.


class Brain:
    """
    Chooses response direction based on emotion and context.
    """

    def decide(self, emotion: str, context: dict) -> str:
        """
        Returns a response mode.
        This will guide ResponseGuide later.
        """

        if emotion in ["tired", "overwhelmed"]:
            return "grounding"

        if emotion in ["anxious", "sad"]:
            return "presence"

        if emotion in ["confused"]:
            return "clarification"

        if emotion in ["avoidant"]:
            return "gentle_reflection"

        return "presence"
