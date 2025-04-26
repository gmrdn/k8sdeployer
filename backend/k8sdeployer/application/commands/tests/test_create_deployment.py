from k8sdeployer.application.commands.create_deployment import CreateDeploymentCommand
from k8sdeployer.infrastructure.fake_deployment_service import FakeDeploymentService



def test_create_deployment_adds_frontend_annotation():
    fake_k8s_service = FakeDeploymentService()

    CreateDeploymentCommand(
        deployment_service=fake_k8s_service,
        name="my-new-deployment",
        image="nginx:latest",
        replicas=2
    )

    created_deployment = fake_k8s_service.created_deployments[0]  # Assuming fake stores creations
    annotations = created_deployment.metadata.annotations

    assert annotations is not None
    assert annotations.get("k8sdeployer/frontend-created") == "true"
    assert created_deployment.metadata.name == "my-new-deployment"
    assert created_deployment.spec.replicas == 2
