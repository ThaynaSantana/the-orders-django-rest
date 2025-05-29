from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.exceptions import ValidationException

from .models import Order
from .serializers import OrderSerializer
from .services import change_order_status


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        try:
            new_status = request.data.get("status")
            order = change_order_status(pk, new_status)
            serializer = self.get_serializer(order)
            return Response(serializer.data)
        except ValidationException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
