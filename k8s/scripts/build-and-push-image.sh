#!/bin/bash

# Builds a docker image for the given dockerfile and pushes it to the
# local  kind cluster registry.

image_name=$1

# Check if the image name is provided
if [ -z "$image_name" ]; then
  echo "Usage: $0 <image_name>"
  exit 1
fi
# Build the docker image
# Check if the service is ollama and pull the latest image from the registry
if [ "$image_name" == "ollama" ]; then
  echo "Pulling the latest ollama image from the registry..."
  docker pull ollama/ollama:latest
  echo "Loading the ollama image into the kind cluster..."
  kind load docker-image ollama/ollama:latest --name pharma-cluster
else
  echo "Building the docker image: $image_name"
  docker build -t ${image_name}:latest -f ${image_name}/Dockerfile ./${image_name}
  kind load docker-image ${image_name}:latest --name pharma-cluster
fi