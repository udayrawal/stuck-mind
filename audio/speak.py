# Responsibility:
# Optional audio output for responses.
# Safe to disable entirely.

from .voice_engine import VoiceEngine


class Speaker:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.engine = VoiceEngine()

    def say(self, text: str, tone: str = "neutral"):
        if not self.enabled:
            return

        self.engine.speak(text, tone)
