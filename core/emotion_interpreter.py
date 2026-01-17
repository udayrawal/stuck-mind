# Responsibility: Infers transient emotional state from text;
# does not persist, diagnose, or label identity.


class EmotionalInterpreter:
    """
    Infers lightweight emotional signals from text.
    Signals are transient and non-authoritative.
    """

    def infer(self, text: str) -> str:
        t = text.lower()

        # Low energy / fatigue
        if any(k in t for k in [
            "exhausted",
            "tired",
            "no energy",
            "drained",
            "burnt out",
            "burned out"
        ]):
            return "tired"

        # Overload / pressure
        if any(k in t for k in [
            "too much",
            "overwhelmed",
            "pressure",
            "piling up",
            "everything at once"
        ]):
            return "overwhelmed"

        # Anxiety / worry
        if any(k in t for k in [
            "worried",
            "anxious",
            "scared",
            "nervous",
            "on edge"
        ]):
            return "anxious"

        # Avoidance / procrastination
        if any(k in t for k in [
            "scrolling",
            "avoiding",
            "putting it off",
            "procrastinating",
            "can't start",
            "stuck"
        ]):
            return "avoidant"

        # Confusion / mental fog
        if any(k in t for k in [
            "confused",
            "unclear",
            "don't know",
            "not sure",
            "lost"
        ]):
            return "confused"

        # Sadness / heaviness
        if any(k in t for k in [
            "sad",
            "low",
            "heavy",
            "down",
            "hopeless"
        ]):
            return "sad"

        # Default neutral presence
        return "neutral"
