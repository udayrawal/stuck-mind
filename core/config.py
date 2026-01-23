# NOTE:
# Defaults are conservative by design.
# Change only after updating tests.

# Responsibility: Centralized configuration and constants.


# ---------- Session / Memory Limits ----------

SHORT_TERM_LIMIT = 5
RECENT_CONTEXT_LIMIT = 3   # single source of truth


# ---------- Safety / Language Rules ----------

# Absolute language that creates pressure or judgment
ABSOLUTE_WORDS = {
    "always",
    "never"
}

# Imperative language that implies force or urgency
IMPERATIVE_WORDS = {
    "should",
    "must",
    "have to",
    "need to"
}


# ---------- Pattern Suggester ----------

MIN_CONTEXT_FOR_PATTERN = 2


# ---------- Fallback Response ----------

SAFE_FALLBACK_RESPONSE = "I’m here. We can take this slowly."


# ---------- Audio / TTS ----------
ENABLE_AUDIO = False
