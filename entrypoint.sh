#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "Retrieving llama3.2 model..."
ollama create pharma_assistant -f ./model_files/Modelfile_pharma_assistant
ollama create language_detector -f ./model_files/Modelfile_language_detector
echo "Done!"

# Wait for Ollama process to finish.
wait $pid