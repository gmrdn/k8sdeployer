from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from k8sdeployer.application.commands.create_deployment import CreateDeploymentCommand
from k8sdeployer.application.queries.list_deployments import ListDeploymentsQuery
from k8sdeployer.infrastructure.kubernetes_service import KubernetesDeploymentService

# Inject real service
deployment_service = KubernetesDeploymentService()

@api_view(['POST'])
def create_deployment_view(request):
    command = CreateDeploymentCommand(
        service=deployment_service,
        name=request.data["name"],
        image=request.data["image"],
        replicas=int(request.data.get("replicas", 1))
    )
    result = command.execute()
    return Response(result, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def list_deployments_view(request):
    query = ListDeploymentsQuery(service=deployment_service)
    result = query.execute()
    return Response(result)
