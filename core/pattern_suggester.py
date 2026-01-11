# Responsibility: Proposes tentative abstract patterns from context; never stores or asserts them.

from .config import MIN_CONTEXT_FOR_PATTERN


class PatternSuggester:

    FORBIDDEN_MARKERS = [
        "on ",
        "at ",
        "yesterday",
        "today",
        "tomorrow",
        "am",
        "pm",
        "202",
        ":"
    ]

    def suggest(self, recent_context: list[str]) -> str | None:
        if len(recent_context) < MIN_CONTEXT_FOR_PATTERN:
            return None


        text = " ".join(recent_context).lower()
        generated_pattern = None

        if "avoid" in text and "start" in text:
            generated_pattern = "Starting feels harder when pressure is high."

        elif "tired" in text and "scroll" in text:
            generated_pattern = "Low energy leads to avoidance through scrolling."

        elif "overwhelmed" in text and "too much" in text:
            generated_pattern = "Tasks feel heavier when they are undefined."

        if not generated_pattern:
            return None

        candidate = generated_pattern.lower()

        if any(marker in candidate for marker in self.FORBIDDEN_MARKERS):
            return None

        return generated_pattern
