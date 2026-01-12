# Responsibility: Verifies MemoryController session cleanup behavior.

from core.memory_controller import MemoryController
from core.memory import Memory
from core.journal import Journal
from core.memory_interface import MemoryInterface


def test_short_term_clears_on_end_session():
    # Arrange: real objects
    journal = Journal()
    memory = Memory()
    rules = MemoryInterface()

    controller = MemoryController(
        journal=journal,
        memory=memory,
        rules=rules
    )

    # Act: simulate session activity
    controller.process_input("I feel tired")
    controller.process_input("I keep scrolling")

    # Sanity check: short-term memory exists
    assert len(memory.short_term) > 0

    # Act: end session
    controller.end_session()

    # Assert: short-term memory cleared
    assert memory.short_term == []
