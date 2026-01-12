# Responsibility: Orchestrates memory flow and enforces rules; never interprets or speaks.

class MemoryController:
    def __init__(self, journal, memory, rules, suggester=None):
        self.journal = journal
        self.memory = memory
        self.rules = rules
        self.suggester = suggester
        self.long_term_candidate = None

    def process_input(self, text: str):
        # 1. Always store raw input
        self.journal.save(text)

        # 2. Short-term memory (rules decide, memory stores)
        if self.rules and self.rules.should_store_short_term(text):
            self.memory.save_short(text)

        # 3. Suggest long-term pattern (NO storage)
        if self.suggester and self.rules:
            context = self.memory.get_context().get("recent_context", [])
            pattern = self.suggester.suggest(context)

            if (
                pattern
                and self.rules.should_store_long_term(pattern)
                and pattern not in self.memory.long_term
            ):
                self.long_term_candidate = pattern

    def end_session(self):
        self.memory.clear_short()
