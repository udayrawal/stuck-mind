class MemoryController:
    """
    Orchestrates memory flow.
    No interpretation.
    No intelligence.
    Enforces memory rules only.
    """

    def __init__(self, journal, memory, rules):
        """
        journal: handles raw append-only storage
        memory: handles short-term and long-term storage
        rules: decides what is allowed to be stored
        """
        self.journal = journal
        self.memory = memory
        self.rules = rules

    def process_input(self, text: str):
        """
        Accepts raw user input and routes it safely.
        """

        # Always store raw text in the journal
        self.journal.save_entry(text)

        # Short-term memory (session-level, if allowed)
        if self.rules and self.rules.allow_short_term(text):
            self.memory.save_short(text)

        # Long-term memory (patterns only, if allowed)
        if self.rules and self.rules.allow_long_term(text):
            self.memory.save_long(text)
