# Rick and Morty API Data Fetcher

This application fetches and serves character data from the "Rick and Morty" API using specific filters.


# Prerequisites
1) Docker installed in the system : https://www.docker.com/
2) Minikube installed in the system and k8s local cluster created with it and running: https://minikube.sigs.k8s.io/docs/start/

# In every subdirectory there is a separate README.md for each step of the assignment on how to run the app. 


# GitHub Actions Workflow

Our CI/CD pipeline includes a GitHub Actions workflow that automates the deployment and testing of the Rick and Morty API Data Fetcher on a local Kubernetes cluster.
Here's a brief overview of the steps involved:

1. Environment Setup
The workflow checks out the latest code from the repository.
It sets up helm the essential tool for deploying applications on Kubernetes.
kind (Kubernetes in Docker) is installed, which provides a lightweight Kubernetes cluster for local testing.
2. Kubernetes Cluster Creation
A new Kubernetes cluster is created using kind.
3. Application Deployment
The Rick and Morty API Data Fetcher is deployed to the Kubernetes cluster using the Helm chart provided in the repository.
4. Testing - Most important step to see that the application actually getting the data. 
Once deployed, the Rick and Morty API Data Fetcher's endpoints are tested to ensure they are functioning as expected. This is achieved by sending HTTP requests to the exposed endpoints.
5. Cleanup
After testing, the local Kubernetes cluster is deleted to free up resources.
For more details on the workflow, you can check the .github/workflows/main.yml file in the repository.
