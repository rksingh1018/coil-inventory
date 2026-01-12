from rest_framework.viewsets import ModelViewSet
from .models import Coil
from .serializers import CoilSerializer

def check_low_stock(coil):
    if coil.is_low_stock():
        print(f"⚠️ Low stock alert for coil {coil.badge_number}")

class CoilViewSet(ModelViewSet):
    queryset = Coil.objects.all()
    serializer_class = CoilSerializer

    def perform_create(self, serializer):
        coil = serializer.save()
        check_low_stock(coil)

    def perform_update(self, serializer):
        coil = serializer.save()
        check_low_stock(coil)
