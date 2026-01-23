# audio/voice_utils.py
from audio.tone import TONES

def validate_tone(tone: str) -> str:
    if not tone:
        return "neutral"
    tone = tone.strip().lower()
    return tone if tone in TONES else "neutral"
