# Rick and Morty API Data Fetcher

This application fetches and serves character data from the "Rick and Morty" API using specific filters.


# Prerequisites
1) Docker installed in the system : https://www.docker.com/
2) Minikube installed in the system and k8s local cluster created with it and running: https://minikube.sigs.k8s.io/docs/start/

# In every subdirectory there is a separate README.md for each step of the assignment on how to run the app. 


## GitHub Actions Workflow: Deploy and test Rick and Morty API Data Fetcher on Kubernetes

This workflow automates the deployment and testing of the "Rick and Morty API Data Fetcher" application on a local Kubernetes cluster using Helm and kind (Kubernetes in Docker). The workflow is triggered on every push to the repository.

### Workflow Structure:

#### 1. **Checkout code**:
   This step checks out the latest version of your code from the repository using the `actions/checkout@v4` action.

#### 2. **Set up Helm**:
   Initializes Helm, the package manager for Kubernetes, using the `azure/setup-helm@v3` action.

#### 3. **Install kind (Kubernetes in Docker)**:
   Installs `kind`, a tool for running local Kubernetes clusters using Docker container nodes. The specific version `v0.20.0` is used in this step.

#### 4. **Testing Kind**:
   This step checks the status of the `kind` cluster by:
   - Displaying cluster information
   - Listing system pods
   - Showing the current Kubernetes context
   - Displaying the environment's kubeconfig
   - Listing Docker images present

#### 5. **Set up Docker Buildx**:
   Initializes Docker Buildx using the `docker/setup-buildx-action@v3` action. Buildx is an extension for building container images.

#### 6. **Build and push Docker image**:
   Builds the Docker image for the "Rick and Morty API Data Fetcher" application using the specified Dockerfile and tags it as `rick-and-morty-app:latest`. The built image is also loaded into the Docker daemon.

#### 7. **Load Docker image into kind cluster**:
   Loads the Docker image into the `kind` cluster, making it available for deployment.

#### 8. **Deploy Rick and Morty API Data Fetcher application using Helm**:
   Uses Helm to deploy the application to the Kubernetes cluster. Overrides the image name and tag to use the locally built Docker image.

#### 9. **Wait for Rick and Morty API Data Fetcher app to be ready and portforward**:
   - Waits for the application's deployment to be ready using Helm and kubectl.
   - Sets up port forwarding from the service to `localhost` on port `5000`.

#### 10. **Run tests**:
   Sends an HTTP request to the application's `/data` endpoint and processes the output using `jq`.

#### 11. **Cleanup**:
   Deletes the `kind` cluster, cleaning up all resources.


