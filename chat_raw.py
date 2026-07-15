import requests 
import json
from models_enum import MODELS 

DEFAULT_MODEL = MODELS.LLAMA3.value
LOCAL_PORT_URL = "http://localhost:11434/api/chat"



def chat(prompt, model=DEFAULT_MODEL):
    response = requests.post(
        LOCAL_PORT_URL,
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        },
        stream=True
    )
    # return response.json()["message"]["content"]
    for line in response.iter_lines():
        chunk = json.loads(line)
        chunk_content = chunk["message"]["content"]
        print(chunk_content, end="", flush=True)
        

chat("Explain your prediction for the final outcome of the FIFA world cup in one paragraph.")
