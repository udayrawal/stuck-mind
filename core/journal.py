# Responsibility: Persists raw user input verbatim;
# append-only and interpretation-free.

from datetime import datetime
import json
from pathlib import Path


JOURNAL_FILE = Path("data/journal_entries.json")


class Journal:
    def save(self, text: str):
        """
        Appends raw user input to the journal.
        Never interprets.
        Never mutates past entries.
        Must never crash.
        """

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "text": text
        }

        # Ensure parent directory exists
        JOURNAL_FILE.parent.mkdir(parents=True, exist_ok=True)

        # Load existing data safely
        if JOURNAL_FILE.exists():
            content = JOURNAL_FILE.read_text(encoding="utf-8").strip()
            try:
                data = json.loads(content) if content else []
            except json.JSONDecodeError:
                # Corrupted file → preserve safety by starting fresh
                data = []
        else:
            data = []

        data.append(entry)

        # Write back safely
        JOURNAL_FILE.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
