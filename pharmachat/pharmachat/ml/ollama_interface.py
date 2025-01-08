import requests
import json
from loguru import logger

class OllamaInterface():
    """Interface to interact with the Ollama local LLM."""

    def __init__(self, model_name = "llama3.2"):
        self.model_name = model_name
        self.api_url = f"http://ollama:11434/api/generate"
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
        }

    def query_ollama(self, prompt: str, context: str) -> str:
        """
        Queries the Ollama local LLM with a given prompt and context.

        Parameters:
            model (str): The name of the Ollama model to use.
            prompt (str): The user question or prompt.
            context (str): The pharmaceutical leaflet text to use as context.

        Returns:
            str: The response from the model.
        """
        output = ""
        payload = {
            "model": self.model_name,
            "prompt": f"Context:\n{context}\n\nQuestion: {prompt}\n\nAnswer:",
        }
        with self.session.post(self.api_url,json=payload,stream=True) as response:

            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        j = json.loads(line.decode('utf-8'))
                        output += j.get("response", "No response from the model.")
                        if j.get("done", True):
                            break
            else:
                logger.error(f"Error querying the model: {response.text}")

        return output.strip()



