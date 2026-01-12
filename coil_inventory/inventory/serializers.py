from rest_framework import serializers
from .models import Coil

class CoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coil
        fields = '__all__'
