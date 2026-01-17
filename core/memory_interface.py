# Responsibility: Defines memory permission rules;
# contains no storage or inference logic.


import re


class MemoryInterface:
    """
    Decides what is allowed to be remembered.

    Does NOT store memory.
    Does NOT interpret emotion.
    Only applies rules.
    """

    # ---------- PUBLIC RULES ----------

    def should_store_short_term(self, text: str) -> bool:
        """
        Short-term memory is allowed if:
        - Text is not marked private
        - Text is NOT an identity-defining statement
        """

        if self._is_private(text):
            return False

        if self._looks_like_identity(text):
            return False

        return True

    def should_store_long_term(self, pattern: str) -> bool:
        """
        Long-term memory is allowed ONLY if:
        - Pattern is non-empty
        - Pattern contains no event/date references
        """

        if not pattern.strip():
            return False

        if self._contains_event_detail(pattern):
            return False

        return True

    # ---------- INTERNAL CHECKS ----------

    def _is_private(self, text: str) -> bool:
        """
        Blocks explicitly private input.
        """
        return "[private]" in text.lower()

    def _looks_like_identity(self, text: str) -> bool:
        """
        Blocks identity fusion and self-labeling.
        Allows emotional states.
        """

        identity_claims = [
            "this is who i am",
            "i am a failure",
            "i am worthless",
            "i am broken",
            "i am useless",
            "i am nothing"
        ]

        lower = text.lower()
        return any(p in lower for p in identity_claims)

    def _contains_event_detail(self, text: str) -> bool:
        """
        Prevents storing specific events, times, or dates.
        Uses word-boundary checks to avoid false positives.
        """

        lower = text.lower()

        # date / time words
        event_words = [
            "yesterday",
            "today",
            "tomorrow",
            "date"
        ]

        if any(word in lower for word in event_words):
            return True

        # time patterns like "10 am", "5 pm", "at 3"
        time_patterns = [
            r"\b\d{1,2}\s?(am|pm)\b",
            r"\bat\s+\d{1,2}\b"
        ]

        return any(re.search(pattern, lower) for pattern in time_patterns)
