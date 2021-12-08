# Salesloft TechOps Exercise

We have two available exercises for you... pick whichever one you prefer.

## Option 1: API

Salesloft is looking to add a random API to our app. Why? I dunno, Product Management is weird.

Anyways, we need to set up a small proxy service so that we can abstract away the provider we use behind the scenes.

The final result will need:
- The initial API
- A Docker-ized application
- Deployment files for Kubernetes

Please use Python for the API. We recommend [Flask](https://flask.palletsprojects.com/) as well.

### Expected API

Your mission, if you choose to accept it, is to create a robust HTTP API with an endpoint that will return some data from any of the APIs available here https://github.com/public-apis/public-apis

Feel free to choose whichever API is interesting to you. If you choose an API that requires an API key **Please don't commit your API key into the repository or publish it to a Docker registry!**

Your API should return JSON

### Deployment

For deployment, we use Kubernetes, so the app will need to run within a Docker container. We don't need to have the container image available publicly as part of submission, but we should be able to build the image.

If you don't have a Kubernetes cluster available, you can run one locally with [Minikube](https://kubernetes.io/docs/setup/minikube/) or [kind](https://github.com/kubernetes-sigs/kind).

In the end, we should be able to add the Kubernetes resources to a cluster and be able to access the API

### Submission

Please submit a tarball of your code and manifests via the Greenhouse upload link. The submission should include:

  * A README file with instructions on how to run the project locally
  * your API source code
  * your Docker file
  * your Kubernetes manifests

## Option 2: Application deployment

Salesloft is trying to find a way to share once off secrets with 3rd parties. We've found an application called [OTS](https://github.com/Luzifer/ots) that seems to suit our needs.

What we want you to do is to write some Ansible/Chef/Puppet/docker-compose/Bash (your choice for which one, we're not fussy... but we use Ansible) for us that configures it in order for us to evaluate the application.

### What we expect

You're welcome to use any of the tools listed above. What we want is a runnable playbook/recipe/manifest that we can point at a VM (or EC2 instance) and get OTS up and running.
We would like OTS to be running behind a nginx reverse proxy, and for it to be configured with Redis as it's datastore.

We have included a sample Vagrantfile in this repo, should you wish to run this locally.

### Submission

Please submit a tarball of your code via the Greenhouse upload link. The submission should include:

  * A README file with instructions on how to run the project
  * your source code
