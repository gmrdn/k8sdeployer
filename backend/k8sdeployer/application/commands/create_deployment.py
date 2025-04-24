class CreateDeploymentCommand:
    def __init__(self, service, name: str, image: str, replicas: int = 1):
        self.service = service
        self.name = name
        self.image = image
        self.replicas = replicas

    def execute(self):
        self.service.create_deployment(self.name, self.image, self.replicas)
        return {"status": "Deployment created"}
