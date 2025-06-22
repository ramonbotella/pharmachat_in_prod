# Creates local kubernetes cluster
create-cluster:
	bash ./k8s/kind/create-cluster.sh

# Builds and pushes the docker image to the given environment
build-and-push:
	bash ./k8s/scripts/build-and-push-image.sh ${image_name}

# Deploys a service to the given environment
deploy:
	bash ./k8s/scripts/deploy.sh ${service}
