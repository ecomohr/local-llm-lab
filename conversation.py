from chat_client import stream_chat

SYSTEM_PROMPT = "You are a helpful, direct assistant. Keep answers concise."

def run_conversation():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("Conversation has started! Yay! Type 'exit' or 'quit' to stop anytime. \n")

    while True:
        print()
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("Ending conversation, thanks for stopping by! :)")
            break

        messages.append({"role": "user", "content": user_input})

        print("Assistant: ", end="", flush=True)
        assistant_reply = stream_chat(messages)

        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    run_conversation()