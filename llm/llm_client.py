import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1"

def call_llm(prompt: str) -> str:
    """
    This function call llm model llama3.1 and generate the steps.
    """
    payload = {
                "model":MODEL_NAME,
                "prompt":prompt,
                "stream":False
              }
    
    response = requests.post(OLLAMA_URL, payload)
    response.raise_for_status()

    return response.json()["response"]