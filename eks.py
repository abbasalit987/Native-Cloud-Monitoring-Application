from kubernetes import client, config

# Load kube config
config.load_kube_config()

# Define the name of the deployment, secret, and namespace
deployment_name = 'my-flask-app'
namespace = 'default'
secret_name = 'my-registry-key'

# Create or update the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name=deployment_name),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="058264451580.dkr.ecr.us-east-1.amazonaws.com/cloud-native-monitoring-app-repo",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ],
                image_pull_secrets=[client.V1LocalObjectReference(name=secret_name)]
            )
        )
    )
)

# Initialize API client
api_instance = client.AppsV1Api()

try:
    # Try to update the existing deployment
    api_instance.replace_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=deployment
    )
    print(f"Deployment '{deployment_name}' updated successfully.")
except client.exceptions.ApiException as e:
    if e.status == 404:
        # If deployment doesn't exist, create it
        api_instance.create_namespaced_deployment(
            namespace=namespace,
            body=deployment
        )
        print(f"Deployment '{deployment_name}' created successfully.")
    else:
        raise
