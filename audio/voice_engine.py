# Responsibility:
# Low-level voice output engine.
# Does not know about emotions, memory, or chat flow.

import json
from pathlib import Path

TONE_FILE = Path(__file__).parent / "tone_profiles.json"


class VoiceEngine:
    def __init__(self):
        if TONE_FILE.exists():
            self.tones = json.loads(TONE_FILE.read_text())
        else:
            self.tones = {}

    def speak(self, text: str, tone: str = "neutral"):
        """
        Placeholder for future TTS.
        Safe no-op for now.
        """
        profile = self.tones.get(tone, {})
        # Later: pass profile to TTS engine
        # For now, we do nothing intentionally
        return
