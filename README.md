# Salesloft TechOps Exercise

We have two available exercises for you... pick whichever one you prefer.

## Option 1: Code Review

Salesloft is looking to find the best starter pokemon. Why? I dunno, Product Management is weird and wants to be the very best.

Anyways, we have setup a small micro-service style application with a split out front and back end.

### Expected 

Your mission, if you choose to accept it, is to code review the `/app` directory. The code works as is, but this is your chance to put a little bit of your creativity and personality into a more efficient solution.

### Submission

Your code review should cover:

  * Python application code
  * Dockerfiles
  * Kubernetes Manifests


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
