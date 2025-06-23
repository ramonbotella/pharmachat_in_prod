# Creates local kubernetes cluster
create-cluster:
	bash ./k8s/kind/create-cluster.sh

# Builds and pushes the docker image to the given environment
build-and-push:
	bash ./k8s/scripts/build-and-push-image.sh ${image_name}

# Deploys a service to the given environment
deploy:
	bash ./k8s/scripts/deploy.sh ${service}

# Run the whole pipeline
pipeline:
	make create-cluster
	make build-and-push image_name=ollama
	make build-and-push image_name=pharmachat
	make build-and-push image_name=pharmachat_frontend
	make deploy service=ollama
	make deploy service=pharmachat
	make deploy service=pharmachat_frontend
	# Run port-forwarding to access the streamlit app in localhost
	# kubectl port-forward service/pharmachat-frontend-service 8501:8501

