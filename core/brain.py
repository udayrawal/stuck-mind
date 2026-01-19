# Responsibility: Decides response mode based on state and context.
# Does NOT generate text.
# Does NOT access memory directly.

class Brain:
    def decide(self, state: str, context: dict) -> str:
        if state in {"tired", "overwhelmed"}:
            return "gentle"

        if state == "anxious":
            return "grounding"

        return "neutral"
