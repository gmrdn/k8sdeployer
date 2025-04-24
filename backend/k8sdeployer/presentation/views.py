from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from k8sdeployer.application.commands.create_deployment import CreateDeploymentCommand
from k8sdeployer.application.queries.list_deployments import ListDeploymentsQuery
from k8sdeployer.infrastructure.kubernetes_service import KubernetesDeploymentService
from django.core.exceptions import ValidationError

# Inject real service
deployment_service = KubernetesDeploymentService()

@api_view(['POST'])
def create_deployment_view(request):
    try:
        command = CreateDeploymentCommand(
            deployment_service=deployment_service,
            name=request.data["name"],
            image=request.data["image"],
            replicas=int(request.data.get("replicas", 1))
        )
        result = command.execute()
        return Response(result, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_deployments_view(request):
    query = ListDeploymentsQuery(deployment_service=deployment_service)
    result = query.execute()
    return Response(result)
