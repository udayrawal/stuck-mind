# NOTE:
# This module stores memory.
# It does not decide what SHOULD be remembered.
# That responsibility belongs to MemoryInterface / MemoryController.

# Responsibility: Stores short-term and long-term memory only;
# does not decide what should be remembered.


"""
========================================
Memory System Design Document
========================================

PURPOSE
- Memory exists to support the user, not control them.
- Memory is used to increase clarity and emotional safety.
- Memory must never shame, pressure, or define identity.

----------------------------------------
SHORT-TERM MEMORY
----------------------------------------
Used only for the present moment.

Stores:
- Today’s mood
- Current problem or thought loop
- What triggered the stuck feeling
- What helped (or didn’t) today

Rules:
- Clears itself naturally.
- No attachment.
- No over-analysis.
- Not used to build history.

----------------------------------------
LONG-TERM MEMORY
----------------------------------------
Used only for patterns, never details.

Stores:
- Repeating stress situations
- Avoidance habits
- Common emotional triggers
- What usually unsticks the user
- What makes things worse

Rules:
- Stores patterns, not events.
- No dates, no timelines, no incident logs.
- No single event is ever stored as long-term memory.

----------------------------------------
PRIVACY RULE (NON-NEGOTIABLE)
----------------------------------------
- Never store anything the user marks as private.
- If unsure whether something is private → do NOT store it.
- Never use memory to emotionally manipulate.
- No language like "you always" or "you never".

----------------------------------------
CORE MEMORY PRINCIPLE
----------------------------------------
"Memory is a map, not a verdict."
========================================
"""


from .config import SHORT_TERM_LIMIT, RECENT_CONTEXT_LIMIT


class Memory:
    def __init__(self):
        # Session-only memory
        self.short_term = []

        # Pattern-only memory
        self.long_term = []

    # ---------- SHORT-TERM MEMORY ----------
    def save_short(self, text: str):
        self.short_term.append(text)

        if len(self.short_term) > SHORT_TERM_LIMIT:
            self.short_term = self.short_term[-SHORT_TERM_LIMIT:]

    def clear_short(self):
        """
        Clears session memory naturally.
        """
        self.short_term = []

    # ---------- LONG-TERM MEMORY (PATTERNS ONLY) ----------
    def save_long(self, pattern: str):
        self.long_term.append(pattern)

    # ---------- CONTEXT FOR AI ----------
    def get_context(self):
        return {
            "recent_context": self.short_term[-RECENT_CONTEXT_LIMIT:],
            "patterns": self.long_term
        }
