from core.memory import Memory

memory = Memory()

def process_user_input(text: str):
    memory.save_entry(text)
    memory.save_short(text)

    context = memory.get_context()
    return context

