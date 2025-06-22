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
echo "Building the docker image: $image_name"
docker build -t ${}image_name}:latest -f ${image_name}/Dockerfile .
kind load docker-image ${image_name}:latest --name pharma-cluster