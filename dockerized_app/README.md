# Rick and Morty API Data Fetcher

This application fetches and serves character data from the "Rick and Morty" API using specific filters.


# Prerequisites
1) Docker installed in the system : https://www.docker.com/
2) Minikube installed in the system and k8s local cluster created with it and running: https://minikube.sigs.k8s.io/docs/start/

## Building the Docker Image

docker build -t rick_and_morty_app .
docker run -p 5000:5000 rick_and_morty_app

## Access the data 
After you run it on the local cluster you can fetch data  on : http://localhost:5000/data