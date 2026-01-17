# Responsibility: Orchestrates memory flow and enforces rules;
# never interprets emotion or generates responses.


class MemoryController:
    def __init__(self, journal, memory, rules, suggester=None):
        self.journal = journal
        self.memory = memory
        self.rules = rules
        self.suggester = suggester

        # Holds a proposed long-term memory (not stored yet)
        self.long_term_candidate = None

    def process_input(self, text: str):
        """
        Routes raw user input through the memory system.
        """

        # 1. Always store raw input
        self.journal.save(text)

        # 2. Short-term memory (rules decide, memory stores)
        if self.rules and self.rules.should_store_short_term(text):
            self.memory.save_short(text)

        # 3. Suggest long-term pattern (NO storage here)
        if self.suggester and self.rules:
            context = self.memory.get_context().get("recent_context", [])
            pattern = self.suggester.suggest(context)

            if (
                pattern
                and pattern.get("confidence", 0) >= 0.6
                and self.rules.should_store_long_term(pattern["text"])
                and self.long_term_candidate is None
            ):
                self.long_term_candidate = pattern

    def end_session(self):
        """
        Clears session-scoped memory.
        """
        self.memory.clear_short()
