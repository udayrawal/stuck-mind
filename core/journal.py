# Responsibility: Persists raw user input verbatim; append-only and interpretation-free.


from datetime import datetime
import json

JOURNAL_FILE = ("data/journal_entries.json")

class Journal:
    def save(self, text: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "text": text
        }

        if JOURNAL_FILE.exists():
            data = json.loads(JOURNAL_FILE.read_text())
        else:
            data = []

        data.append(entry)
        JOURNAL_FILE.write_text(json.dumps(data, indent=2))
