# Responsibility: Defines memory permission rules; contains no storage or inference logic.


class MemoryInterface:
    """
    Decides what is allowed to be remembered.

    Does NOT store memory.
    Does NOT interpret emotion.
    Only applies rules.
    """

    def should_store_short_term(self, text: str) -> bool:
        if self._is_private(text):
            return False

        if self._looks_like_identity(text):
            return False

        return True

    def should_store_long_term(self, pattern: str) -> bool:
        if not pattern.strip():
            return False
        
        if self._contains_event_detail(pattern):
            return False

        return True

    # --- internal rule checks ---

    def _is_private(self, text: str) -> bool:
        return "[private]" in text.lower()

    def _looks_like_identity(self, text: str) -> bool:
        banned_phrases = ["i am", "i'm", "this is who i am"]
        return any(p in text.lower() for p in banned_phrases)

    def _contains_event_detail(self, text: str) -> bool:
        banned_markers = ["on ", "at ", "yesterday", "today", "date"]
        return any(m in text.lower() for m in banned_markers)
