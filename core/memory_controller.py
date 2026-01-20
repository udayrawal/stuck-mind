# Responsibility: Orchestrates memory flow and enforces rules; never interprets or speaks.

class MemoryController:
    def __init__(self, journal, memory, rules, suggester=None):
        self.journal = journal
        self.memory = memory
        self.rules = rules
        self.suggester = suggester

        # Holds a proposed long-term memory (not stored yet)
        self.long_term_candidate = None

    def process_input(self, text: str):
        # 1. Always store raw input
        self.journal.save(text)

        # 2. Short-term memory (rules decide, memory stores)
        if self.rules and self.rules.should_store_short_term(text):
            self.memory.save_short(text)

        # 3. Suggest long-term pattern (NO storage here)
        if not self.suggester:
            return

        context = self.memory.get_context().get("recent_context", [])
        pattern = self.suggester.suggest(context)

        # 🔒 HARD GUARD — fixes your crash
        if not isinstance(pattern, dict):
            return

        confidence = pattern.get("confidence", 0)

        if confidence >= 0.6 and self.long_term_candidate is None:
            self.long_term_candidate = pattern
            print("[debug] long_term_candidate set:", pattern["text"])

    def end_session(self):
        self.memory.clear_short()
