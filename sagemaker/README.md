# SageMaker deployment notes

This folder is a deployment starting point, not a one-click deployment. You need an AWS
account with SageMaker, ECR, and S3 permissions and an approved region/instance type.

## Important architecture note
The main local demo uses TorchServe. This SageMaker example uses a custom inference
container contract (`/ping` and `/invocations`) and the same DistilGPT2 generation logic.
If your faculty requires TorchServe specifically inside SageMaker, deploy a
TorchServe-compatible inference image and configure it explicitly; do not describe this
generic container as TorchServe.

## Build and push
1. Create an ECR repository.
2. Authenticate Docker to ECR using the AWS CLI.
3. Build this directory's Dockerfile and tag/push it to ECR.
4. Upload model artifacts if you choose to bake them into the image or adapt the container
   to load them from S3.
5. Create a SageMaker Model, EndpointConfig, and Endpoint with the image URI.
6. Invoke the endpoint with JSON:
   `{"prompt":"A student opened the old classroom door","max_new_tokens":60,"temperature":0.8}`

For a student demonstration, use the smallest faculty-approved instance and delete the
endpoint immediately after testing. Endpoint uptime is billable.
