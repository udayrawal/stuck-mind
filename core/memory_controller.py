class MemoryController:
    def __init__(self, journal, memory, rules):
        self.journal = journal
        self.memory = memory
        self.rules = rules

    def process(self, text: str):
        self.journal.save(text)

        if self.rules.should_store_short_term(text):
            self.memory.save_short(text)
        if self.rules.should_store_long_term(text):
            self.memory.save_long(text) 

            