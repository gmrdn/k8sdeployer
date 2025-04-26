from kubernetes import client, config
from k8sdeployer.domain.deployment_service import DeploymentService

class KubernetesDeploymentService(DeploymentService):
    def __init__(self):
        config.load_kube_config()
        self.api = client.AppsV1Api()

    def create_deployment(self, name: str, image: str, replicas: int, annotation: str):
        container = client.V1Container(
            name=name,
            image=image,
            ports=[client.V1ContainerPort(container_port=80)],
        )
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": name}),
            spec=client.V1PodSpec(containers=[container]),
        )
        spec = client.V1DeploymentSpec(
            replicas=replicas,
            template=template,
            selector={"matchLabels": {"app": name}},
        )
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(
                name=name,
                annotations={
                    annotation: "true"
                    }
                ),
            spec=spec,
        )
        self.api.create_namespaced_deployment(namespace="default", body=deployment)

    def list_deployments(self):
        deployments = self.api.list_namespaced_deployment(namespace="default")
        return [
            {
                "name": item.metadata.name,
                "replicas": item.spec.replicas,
                "image": item.spec.template.spec.containers[0].image,
                "annotations": item.metadata.annotations,
            }
            for item in deployments.items
        ]
