from abc import ABC, abstractmethod

class DeploymentService(ABC):
    @abstractmethod
    def create_deployment(self, name: str, image: str, replicas: int, annotaion: str):
        pass

    @abstractmethod
    def list_deployments(self):
        pass
