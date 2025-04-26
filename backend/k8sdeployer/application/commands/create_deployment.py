from k8sdeployer.domain.deployment_service import DeploymentService
from django.core.exceptions import ValidationError

class CreateDeploymentCommand:
    def __init__(self, deployment_service: DeploymentService, name: str, image: str, replicas: int = 1):
        self.deployment_service = deployment_service
        self.name = name
        self.image = image
        self.replicas = replicas

    def execute(self):
        try:
            if not self.name or not self.image:
                raise ValueError("Name and image are required fields.")
            if self.replicas < 1:
                raise ValueError("Replicas must be at least 1.")

            self.deployment_service.create_deployment(self.name, self.image, self.replicas, "k8sdeployer/frontend-created")
            return {"status": "Deployment created"}
        except ValueError as e:
            raise ValidationError(str(e))


            
