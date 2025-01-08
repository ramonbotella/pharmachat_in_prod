"""CLI to ask Ollama a question."""

from typer import Typer, Argument
from loguru import logger
from pharmachat.ml.ollama_interface import OllamaInterface
from pharmachat.data.leaflet_scrapping import get_medicament_leaflet

app = Typer()

@app.command(
    help="Ask Ollama a question about a specific medicament."
)
def pharma_assistant(
        medicament: str = Argument(...,help="Exact name of the medicament"),
        question: str = Argument(...,help="Question to ask Ollama model"),
):
    """CLI to ask Ollama a question.

    This command allows the user to ask a question to the Ollama model
    using the leaflet of a specific medicament as context.

    Parameters:
        model (str): The name of the Ollama model to use.
        medicament (str): The exact name of the medicament to use.
        question (str): The question to ask the Ollama model.
    """

    # Get the leaflet text for the medicament
    leaflet = get_medicament_leaflet(medicament)

    if leaflet:
        # Initialize the Ollama interface
        ollama = OllamaInterface()
        response = ollama.query_ollama(question, leaflet)
        logger.info(response)
    else:
        logger.info(f"Error: Unable to fetch leaflet for '{medicament}'.")

if __name__ == "__main__":
    app()