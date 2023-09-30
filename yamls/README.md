# Deploying to Kubernetes

Ensure you have `kubectl` configured to interact with your Kubernetes cluster.


To install the appplication on k8s:
1) kubectl apply -f yamls/
2) minikube service rick-and-morty-app-service
3) Access the /data route in the URL that you got from the previous step for example : http://127.0.0.1:51287/data
NOTE: The port can be different from the the example URL. 


To delete appplication on k8s:

kubectl delete -f yamls/
