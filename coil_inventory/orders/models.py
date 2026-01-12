from django.db import models
from django.contrib.auth.models import User
from inventory.models import Coil

class SalesOrder(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(
        SalesOrder, related_name='items', on_delete=models.CASCADE
    )
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
