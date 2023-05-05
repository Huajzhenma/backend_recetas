from rest_framework import serializers
from .models import Cocina

class CocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocina
        fields = ('id','name', 'description')
