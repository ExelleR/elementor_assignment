# Rick and Morty API Data Fetcher - Helm chart

Install:
1) helm install app-rick-and-morty-app ./Helm

Delete:
1) helm delete app-rick-and-morty-app 
2) minikube service rick-and-morty-app-service
3) Access the /data route in the URL that you got from the previous step for example : http://127.0.0.1:51287/data
NOTE: The port can be different from the the example URL. 