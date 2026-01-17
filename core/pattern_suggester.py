# Responsibility: Proposes tentative abstract patterns from context;
# never stores or asserts them.

from .config import MIN_CONTEXT_FOR_PATTERN


class PatternSuggester:

    FORBIDDEN_MARKERS = [
        "on ",
        "at ",
        "yesterday",
        "today",
        "tomorrow",
        "am ",
        "pm ",
        "202",
        ":"
    ]

    def suggest(self, recent_context: list[str]) -> dict | None:
        """
        Suggests an abstract pattern based on recent short-term context.
        Returns a structured pattern dict or None.
        """

        # Guard 1: not enough context
        if len(recent_context) < MIN_CONTEXT_FOR_PATTERN:
            return None

        text = " ".join(recent_context).lower()
        pattern_text = None

        # --- pattern detection rules ---
        if "avoid" in text and "start" in text:
            pattern_text = "Starting feels harder when pressure is high."

        elif "tired" in text and "scroll" in text:
            pattern_text = "Low energy leads to avoidance through scrolling."

        elif "overwhelmed" in text and "too much" in text:
            pattern_text = "Tasks feel heavier when they are undefined."

        # Guard 2: no pattern detected
        if not pattern_text:
            return None

        lowered_pattern = pattern_text.lower()

        # Guard 3: block event / date leakage
        if any(marker in lowered_pattern for marker in self.FORBIDDEN_MARKERS):
            return None

        # Confidence grows with evidence, capped safely
        evidence_count = len(recent_context)
        confidence = min(0.4 + 0.15 * evidence_count, 0.9)

        return {
            "text": pattern_text,
            "confidence": confidence,
            "evidence_count": evidence_count
        }
