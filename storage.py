import json
import os

CONVERSATION_PATH = "conversation.json"

def save_conversation(msgs, path=CONVERSATION_PATH):
    with open(path, "w") as f:
        json.dump(msgs, f, indent=2)

def load_conversation(path=CONVERSATION_PATH):
    if not os.path.exists(path):
        return None
    try:
        with open(path) as f:
            content = f.read().strip()
            if not content:
                return None
            return json.loads(content)
    except json.JSONDecodeError:
        return None

