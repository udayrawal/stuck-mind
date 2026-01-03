# NOTE:
# This module stores memory.
# It does not decide what SHOULD be remembered.
# That responsibility belongs to MemoryInterface / MemoryController.

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

Examples:
✔ "You get stuck when tasks feel undefined"
✖ "On 12 Jan you failed to start X"

----------------------------------------
PRIVACY RULE (NON-NEGOTIABLE)
----------------------------------------
- Never store anything the user marks as private.
- If unsure whether something is private → do NOT store it.
- Never use memory to emotionally manipulate.
- No language like "you always" or "you never".

This rule overrides all others.

----------------------------------------
HOW STUCK MIND USES MEMORY
----------------------------------------
- To recognize, not judge.
- To gently reflect patterns.
- To avoid repeating advice that doesn’t work.
- To reduce mental noise, not create labels.

Memory is referenced softly, never asserted as fact.

Example tone:
"This feels familiar. Last time, slowing down helped."

----------------------------------------
WHAT MEMORY MUST NEVER DO
----------------------------------------
- No shaming with the past.
- No forcing consistency.
- No absolute language.
- No storing raw emotional confessions.
- No identity formation ("this is who you are").

Memory must never harden into personality.

----------------------------------------
CORE MEMORY PRINCIPLE
----------------------------------------
"Memory is a map, not a verdict."

----------------------------------------
ONE-LINE SYSTEM RULE
----------------------------------------
"Remember only what helps the user feel understood next time."

========================================
END OF MEMORY SYSTEM
========================================
"""

from datetime import datetime
import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")


class Memory:
    def __init__(self):
        # Session-only memory
        self.short_term = []

        # Pattern-only memory
        self.long_term = []

    # ---------- RAW JOURNAL (PRIVATE, APPEND-ONLY) ----------
    def save_entry(self, text: str):
        """
        Stores raw user text.
        No interpretation.
        Never used directly by AI responses.
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "text": text
        }

        if MEMORY_FILE.exists():
            content = MEMORY_FILE.read_text().strip()
            data = json.loads(content) if content else []
        else:
            data = []

        data.append(entry)
        MEMORY_FILE.write_text(json.dumps(data, indent=2))

    # ---------- SHORT-TERM MEMORY ----------
    def save_short(self, text: str):
        """
        Stores immediate context for current session.
        """
        self.short_term.append(text)

        # Optional hard limit
        if len(self.short_term) > 5:
            self.short_term = self.short_term[-5:]

    def clear_short(self):
        """
        Clears session memory naturally.
        """
        self.short_term = []

    # ---------- LONG-TERM MEMORY (PATTERNS ONLY) ----------
    def save_long(self, pattern: str):
        """
        Stores abstract patterns only.
        Must not include events, dates, or identity.
        """
        self.long_term.append(pattern)

    # ---------- CONTEXT FOR AI ----------
    def get_context(self):
        """
        Returns safe, minimal context for the AI.
        """
        return {
            "recent_context": self.short_term[-3:],
            "patterns": self.long_term
        }
