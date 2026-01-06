class MemoryController:
    """
    Orchestrates memory flow.
    No interpretation.
    No intelligence.
    Enforces memory rules only.
    """

    def __init__(self, journal, memory, rules, suggester=None):
        """
        journal: handles raw append-only storage
        memory: handles short-term storage
        rules: decides what is allowed
        suggester: proposes possible long-term patterns
        """
        self.journal = journal
        self.memory = memory
        self.rules = rules
        self.suggester = suggester

        # Holds a proposed long-term memory (not stored)
        self.long_term_candidate = None

    def process_input(self, text: str):
        """
        Accepts raw user input and routes it safely.
        """

        # 1. Always store raw text
        self.journal.save_entry(text)

        # 2. Short-term memory (if allowed)
        if self.rules and self.rules.allow_short_term(text):
            self.memory.save_short(text)

        # 3. Suggest long-term pattern (NO storage)
        if self.suggester:
            context = self.memory.get_context().get("recent_context", [])
            pattern = self.suggester.suggest(context)

            if pattern and self.rules and self.rules.should_store_long_term(pattern):
                self.long_term_candidate = pattern
    
    def end_session(self):
        """
        Clears session-scoped memory at session end.
        """
        self.memory.clear_short()