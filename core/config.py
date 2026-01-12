# NOTE: Defaults are conservative by design.
# Change only after updating tests.


# Responsibility: Centralized configuration and constants.



# Session / memory limits
SHORT_TERM_LIMIT = 5
RECENT_CONTEXT_LIMIT = 3

# Safety / languagebased rules
ABSOLUTE_WORDS = {"always", "never"}
IMPERATIVE_WORDS = {"should", "try", "do", "must"}

# Pattern suggester
MIN_CONTEXT_FOR_PATTERN = 2
RECENT_CONTEXT_WINDOW = 3

# Fallback response
SAFE_FALLBACK_RESPONSE = "I’m here. We can take this slowly."
