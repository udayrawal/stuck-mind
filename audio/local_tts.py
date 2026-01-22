# Responsibility: Local text-to-speech (best-effort, non-blocking)

import threading
import pyttsx3
from .speaker import Speaker

class LocalTTSSpeaker(Speaker):
    def __init__(self):
        self.engine = pyttsx3.init()
        self._configure()

    def _configure(self):
        self.engine.setProperty("rate", 160)
        self.engine.setProperty("volume", 0.9)

    def speak(self, text: str, tone: str = "neutral"):
        def _run():
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass  # audio must never crash chat

        threading.Thread(target=_run, daemon=True).start()
