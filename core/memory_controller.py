# Responsibility: Orchestrates memory flow and enforces rules; never interprets or speaks.
from .memory import Memory

class MemoryController:

    def __init__(self, journal, memory, rules, suggester=None):
        
        self.journal = journal
        self.memory = memory
        self.rules = rules
        self.suggester = suggester

        # Holds a proposed long-term memory (not stored)
        self.long_term_candidate = None

    def process_input(self, text: str):
        self.journal.save(text)

        # 2. Short-term memory (if allowed)
        if self.rules and self.rules.should_store_short_term(text):
            self.memory.save_short(text)


        # 3. Suggest long-term pattern (NO storage)
        if self.suggester and self.rules:
            context = self.memory.get_context().get("recent_context", [])
            pattern = self.suggester.suggest(context)

            # Guard: allow suggestion only if rule allows and not duplicate
            if (
                pattern
                and self.rules.should_store_long_term(pattern)
                and pattern not in self.memory.long_term
            ):
                self.long_term_candidate = pattern

    def end_session(self):
        """
        Clears session-scoped memory at session end.
        """
        self.memory.clear_short()
