# SalesLoft TechOps Exercise

SalesLoft is looking to add weather information to our app. Why? I dunno, Product Management is weird. 

Anyways, we need to set up a small proxy service so that we can abstract away the provider we use behind the scenes.  

The final result will need:
- The initial API
- A basic test suite
- A Docker-ized application
- Deployment files for Kubernetes

Please use Python and [pytest](https://docs.pytest.org/en/stable/) for the API and test suite. We recommend [Flask](https://flask.palletsprojects.com/en/1.1.x/) as well.

## Expected API

Your mission, if you choose to accept it, is to create an HTTP API with the endpoint /station that will return all of the NOAA stations for a given state when passed a state code via a GET. The official NOAA API documentation can be found [here](https://www.ncdc.noaa.gov/cdo-web/webservices/v2#stations)

You will need to [get your own API key from NOAA](https://www.ncdc.noaa.gov/cdo-web/token), but they are free. **Please don't commit your API key into the repository or publish it to a Docker registry!**

`/station?state=<state_code>` is the expected input for a given call (e.g., `/station?state=GA`), where the value of the state parameter is the USPS state code for a given state

The API call should return JSON with the requested state and associated request metadata, as well as all of the stations in that state. The response should look like this:
```json
{
  "requestTime": "2018-01-23T00:00:00-4000",
  "responseTime": "2018-01-23T00:00:00-4000",
  "state": "AZ",
  "results": 1028,
  "offset": 1,
  "limit": 25,
  "stations": [
    {
      ...
    },
    ...
  ]
}
```

## Deployment

For deployment, we use Kubernetes, so the app will need to run within a Docker container. We don't need to have the container image available publicly, just this repository.

If you don't have a Kubernetes cluster available, you can run one locally with [Minikube](https://kubernetes.io/docs/setup/minikube/) or [kind](https://github.com/kubernetes-sigs/kind).

In the end, we should be able to add the Kubernetes resources to a cluster and be able to access the API. Additionally, we should be able to run a suite of passing unit tests locally.

## Submission

Please clone this repo and submit via Greenhouse. The submission should include:

  * A link to your cloned GitHub repo
  * A README file with instructions on how to run the project locally
