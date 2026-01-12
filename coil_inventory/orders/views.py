from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from inventory.models import Coil
from .models import SalesOrder, SalesOrderItem
from .serializers import SalesOrderSerializer

class SalesOrderCreate(APIView):

    @transaction.atomic
    def post(self, request):
        items = request.data.get('items')

        order = SalesOrder.objects.create(created_by=request.user)

        for item in items:
            coil = Coil.objects.select_for_update().get(id=item['coil'])
            qty = item['quantity']

            if coil.quantity < qty:
                raise ValidationError("Insufficient inventory")

            coil.quantity -= qty
            coil.save()

            SalesOrderItem.objects.create(
                sales_order=order,
                coil=coil,
                quantity=qty
            )

        return Response(SalesOrderSerializer(order).data)
