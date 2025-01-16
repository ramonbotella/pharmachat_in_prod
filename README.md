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

## Setup Instructions

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