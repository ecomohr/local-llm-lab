from chat_client import stream_chat
from storage import save_conversation, load_conversation

SYSTEM_PROMPT = "You are a helpful, direct assistant. Keep answers concise."

def run_conversation():
    messages = load_conversation()
    if messages:
        print(f"Resumed conversation with {len(messages)} prior messages.\n")
    else:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        print("Conversation has started! Yay! Type 'exit' or 'quit' to stop anytime. \n")

    while True:
        print()
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit"):
            save_conversation(messages)
            print("Ending conversation, thanks for stopping by! :)")
            break

        messages.append({"role": "user", "content": user_input})

        print("Assistant: ", end="", flush=True)
        assistant_reply = stream_chat(messages)

        messages.append({"role": "assistant", "content": assistant_reply})

        save_conversation(messages)


if __name__ == "__main__":
    run_conversation()

