# PharmaChat in Production

This repository contains the production setup for the PharmaChat application. It includes Docker configurations and necessary scripts to deploy the application.

## Project Structure

- `docker-compose.yaml`: Docker Compose file to set up the multi-container application.
- `pharmachat/`: Directory containing the PharmaChat backend service.
- `pharmachat_frontend/`: Directory containing the PharmaChat frontend service.
- `entrypoint.sh`: Script to initialize the `ollama` service.
- `model_files/`: Directory containing model files for the `ollama` service.

## Services

### ollama

- **Image**: `ollama/ollama`
- **Ports**: `11434:11434`
- **Volumes**:
  - `ollama_data:/root/.ollama`
  - `./entrypoint.sh:/entrypoint.sh`
  - `./model_files:/model_files`
- **Entrypoint**: `/usr/bin/bash /entrypoint.sh`

### pharmachat

- **Build Context**: `./pharmachat`
- **Dockerfile**: `Dockerfile`
- **Ports**: `8000:8000`
- **Volumes**: `./pharmachat:/root`
- **Depends On**: `ollama`

### pharmachat_frontend

- **Build Context**: `./pharmachat_frontend`
- **Dockerfile**: `Dockerfile`
- **Ports**: `8501:8501`
- **Volumes**: `./pharmachat_frontend:/app`
- **Depends On**: `pharmachat`

## Setup Instructions for Docker Deployment

1. Clone the repository:
    ```sh
    git clone https://github.com/ramonbotella/pharmachat_in_prod.git
    cd pharmachat_in_prod
    ```

2. Build and start the services:
    ```sh
    docker compose up -d
    ```

3. Access the services:
    - PharmaChat Backend: `http://localhost:8000`
    - PharmaChat Frontend: `http://localhost:8501`
    - Ollama API: `http://localhost:11434/api/generate`

## Setup Instructions for Kind Kubernetes Deployment
To deploy the PharmaChat application to a local Kubernetes cluster using Kind, follow these steps. Ensure you have Docker, Kind, kubectl, and make installed on your system.

1. Clone this repository:
    ```sh
    git clone https://github.com/ramonbotella/pharmachat_in_prod.git
    cd pharmachat_in_prod
    ```

2. Deploy the entire application pipeline. The Makefile in the root of this repository automates the entire deployment process, including cluster creation, image building/loading, and service deployment.
    ```
    make pipeline
    ```
This command will:
- Delete any existing pharma-cluster and its associated Docker network, then create a new Kind cluster with port mapping enabled.
- Pull the ollama/ollama:latest image and load it into the Kind cluster.
- Build the pharmachat:latest and pharmachat_frontend:latest Docker images from their respective Dockerfiles and load them into the Kind cluster.
- Apply the Kubernetes deployment and service manifests for ollama, pharmachat, and pharmachat_frontend to the cluster.

3. Access the PharmaChat Frontend:
Once the make pipeline command completes, the pharmachat_frontend service will be running in your Kind cluster. Due to the port mapping defined in kind-with-portmapping.yaml, you can access it directly via http://localhost:8501.

Alternatively, if make pipeline does not automatically open the port (or if you need to re-establish it), you can manually forward the port:

```sh
kubectl port-forward service/pharmachat-frontend-service 8501:8501
```

Then, open your web browser and navigate to http://localhost:8501.

## Configuration

The configuration for the PharmaChat backend can be found in `pharmachat/pharmachat/config/config.yaml`. Update the URLs and other settings as needed.

## Troubleshooting

- Ensure Docker and Docker Compose are installed and running.
- Check the logs of the services for any errors:
    ```sh
    docker compose logs <service-name>
    ```
## Author

- **Name**: Ramon Botella Nieto
- **Email**: rbnieto@gmail.com

## License

This project is licensed under the MIT License.