#!/bin/bash

# Deploys the application to the local kind cluster.
service=$1

# Check if the kind cluster is running
if ! kubectl cluster-info &> /dev/null; then
  echo "Kind cluster is not running. Please start the cluster first."
  exit 1
fi

# Apply the Kubernetes manifests
echo "Applying Kubernetes manifests..."
kubectl delete -f ./k8s/${service}/${service}-deployment.yaml --ignore-not-found=true
kubectl apply -f ./k8s/${service}/${service}-deployment.yaml
