from k8sdeployer.domain.deployment_service import DeploymentService

class FakeDeploymentService(DeploymentService):
    def __init__(self):
        self._deployments = []

    def create_deployment(self, name: str, image: str, replicas: int):
        self._deployments.append({
            "name": name,
            "image": image,
            "replicas": replicas,
        })

    def list_deployments(self):
        return self._deployments
