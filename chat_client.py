import requests 
import json
from models_enum import MODELS 

DEFAULT_MODEL = MODELS.LLAMA3.value
LOCAL_PORT_URL = "http://localhost:11434/api/chat"



def stream_chat(messages, model=DEFAULT_MODEL):
    """
    Sends the full message history to Ollama and streams the response
    back in chunks.
    """
    response = requests.post(
        LOCAL_PORT_URL,
        json={
            "model": model,
            "messages": messages,
            "stream": True
        },
        stream=True
    )
    # return response.json()["message"]["content"]
    for line in response.iter_lines():
        chunk = json.loads(line)
        chunk_content = chunk["message"]["content"]
        print(chunk_content, end="", flush=True)
        

# chat("Explain your prediction for the final outcome of the FIFA world cup in one paragraph.")
