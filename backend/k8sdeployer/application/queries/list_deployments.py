from k8sdeployer.domain.deployment_service import DeploymentService

class ListDeploymentsQuery:
    def __init__(self, deployment_service: DeploymentService):
        self.deployment_service = deployment_service

    def execute(self):
        return self.deployment_service.list_deployments()
