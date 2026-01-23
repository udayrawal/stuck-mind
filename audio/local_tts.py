# audio/local_tts.py
import json
import threading
import logging
from pathlib import Path
import pyttsx3

from .voice_utils import validate_tone

HERE = Path(__file__).parent
TONE_PROFILES_PATH = HERE / "tone_profiles.json"

log = logging.getLogger("local_tts")
log.addHandler(logging.NullHandler())

class LocalTTSSpeaker:
    """
    Local TTS speaker.
    - Validates tone using voice_utils.validate_tone
    - Loads tone profiles from audio/tone_profiles.json
    - Plays audio in a background thread (non-blocking)
    """

    def __init__(self):
        # load profiles
        self.profiles = self._load_profiles()
        # engine initialised on demand for reliability
        self._engine = None

    def _load_profiles(self):
        if not TONE_PROFILES_PATH.exists():
            # fallback default profiles
            return {
                "neutral": {"rate": 165, "volume": 0.9, "pause": "medium"},
                "soft": {"rate": 145, "volume": 0.8, "pause": "long"},
                "warm": {"rate": 160, "volume": 1.0, "pause": "medium"},
                "grounding": {"rate": 135, "volume": 0.85, "pause": "long"},
            }
        try:
            return json.loads(TONE_PROFILES_PATH.read_text())
        except Exception as e:
            log.exception("Failed to load tone profiles, using defaults: %s", e)
            return {}

    def _ensure_engine(self):
        if self._engine is None:
            try:
                self._engine = pyttsx3.init()
            except Exception:
                log.exception("pyttsx3 init failed")
                self._engine = None

    def speak(self, text: str, tone: str = "neutral"):
        """
        Public non-blocking method.
        Validates tone, finds profile, then spawns a background thread to play audio.
        """
        chosen_tone = validate_tone(tone)
        profile = self.profiles.get(chosen_tone, {})

        # launch background thread so speak is non-blocking for the chat loop
        thread = threading.Thread(target=self._play, args=(text, profile, chosen_tone), daemon=True)
        thread.start()

    def _play(self, text: str, profile: dict, tone: str):
        """
        Blocking playback on background thread — does not throw to caller.
        """
        try:
            self._ensure_engine()
            if not self._engine:
                return

            # set properties
            rate = profile.get("rate")
            volume = profile.get("volume")
            if rate is not None:
                try:
                    self._engine.setProperty("rate", int(rate))
                except Exception:
                    log.debug("failed to set rate")

            if volume is not None:
                try:
                    self._engine.setProperty("volume", float(volume))
                except Exception:
                    log.debug("failed to set volume")

            # Add a short pause based on profile 'pause' field
            pause_type = profile.get("pause", "medium")
            pause_text = ""
            if pause_type == "long":
                pause_text = " ... "
            elif pause_type == "medium":
                pause_text = " . "
            else:
                pause_text = " "

            speak_text = f"{text}{pause_text}"

            self._engine.say(speak_text)
            self._engine.runAndWait()

        except Exception:
            log.exception("TTS playback failed (swallowed):")
