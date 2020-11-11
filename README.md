# SalesLoft TechOps Exercise

SalesLoft is looking to add a random API to our app. Why? I dunno, Product Management is weird. 

Anyways, we need to set up a small proxy service so that we can abstract away the provider we use behind the scenes.  

The final result will need:
- The initial API
- A Docker-ized application
- Deployment files for Kubernetes

Please use Python for the API. We recommend [Flask](https://flask.palletsprojects.com/en/1.1.x/) as well.

## Expected API

Your mission, if you choose to accept it, is to create an HTTP API with an endpoint that will return some data from any of the APIs available here https://github.com/public-apis/public-apis

Feel free to choose whichever API is interesting to you. If you choose an API that requires an API key **Please don't commit your API key into the repository or publish it to a Docker registry!**

The API call should return JSON 

## Deployment

For deployment, we use Kubernetes, so the app will need to run within a Docker container. We don't need to have the container image available publicly as part of submission, but we should be able to build the image.

If you don't have a Kubernetes cluster available, you can run one locally with [Minikube](https://kubernetes.io/docs/setup/minikube/) or [kind](https://github.com/kubernetes-sigs/kind).

In the end, we should be able to add the Kubernetes resources to a cluster and be able to access the API

## Submission

Please submit a tarball of your code and manifests via the Greenhouse upload link. The submission should include:

  * A README file with instructions on how to run the project locally
  * your API source code
  * your docker file
  * your kubernetes manifests
