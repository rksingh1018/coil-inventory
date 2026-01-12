from django.db import models

class Coil(models.Model):
    badge_number = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    low_stock_threshold = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_low_stock(self):
        return self.quantity < self.low_stock_threshold
