"""
========================================
Memory System v1 (Human-Centered)
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


def save_thought(text):
    with open("data/journal.txt", "a") as f:
        f.write(text + "\n")
