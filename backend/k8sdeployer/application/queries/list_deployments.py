from k8sdeployer.domain.deployment_service import DeploymentService

class ListDeploymentsQuery:
    def __init__(self, deployment_service: DeploymentService):
        self.deployment_service = deployment_service

    def execute(self):
        deployments = self.deployment_service.list_deployments()
        return [
            d for d in deployments
            if d["annotations"] and d["annotations"].get("k8sdeployer/frontend-created") == "true"
            ]
