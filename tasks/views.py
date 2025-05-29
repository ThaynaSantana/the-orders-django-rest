from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.decorators import validate_json

from .serializers import TaskEnqueueSerializer
from .services import enqueue_example_task, enqueue_risky_task


class TaskEnqueueView(APIView):
    """
    View para enfileirar uma tarefa.
    """

    @validate_json(["param"])
    def post(self, request):
        serializer = TaskEnqueueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_id = enqueue_example_task(serializer.validated_data["param"])
        return Response({"job_id": job_id}, status=status.HTTP_202_ACCEPTED)


class RiskyTaskView(APIView):
    def post(self, request):
        job_id = enqueue_risky_task()
        return Response({"job_id": job_id}, status=status.HTTP_202_ACCEPTED)
