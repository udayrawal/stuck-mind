from urllib import response
from memory_controller import MemoryController
from memory import Memory
from emotion_interpreter import EmotionalInterpreter


RESPONSES = {
    "tired": "I hear how drained this feels.",
    "overwhelmed": "That sounds like a lot to carry right now.",
    "anxious": "It makes sense that this feels uneasy.",
    "neutral": "I’m here. Go on."
}


def chat_loop():
    print("Stuck Mind is here.")
    print("Say anything. Type 'exit' to stop.")

    memory = Memory()
    memory_controller = MemoryController(
        journal=memory,
        memory=memory,
        rules=None  # placeholder for now
    )

    emotion_interpreter = EmotionalInterpreter()

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("I'm here whenever you return.")
            break

        # 1. Silent emotional inference (no storage, no output)
        state = emotion_interpreter.infer(user_input)

        # 2. Memory routing (unchanged)
        memory_controller.process_input(user_input)

        # 3. Context retrieval (unchanged)
        context = memory.get_context()

        # 4. Neutral presence response (unchanged)
        response = RESPONSES.get(state, RESPONSES["neutral"])
        print(response)



if __name__ == "__main__":
    chat_loop()
