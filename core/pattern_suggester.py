class PatternSuggester:
    """
    Suggests abstract patterns from recent context.
    Suggestions are tentative and non-binding.
    """

    def suggest(self, recent_context: list[str]) -> str | None:
        text = " ".join(recent_context).lower()

        if "avoid" in text and "start" in text:
            return "Starting feels harder when pressure is high."

        if "tired" in text and "scroll" in text:
            return "Low energy leads to avoidance through scrolling."

        if "overwhelmed" in text and "too much" in text:
            return "Tasks feel heavier when they are undefined."

        return None
