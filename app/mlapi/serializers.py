from rest_framework import serializers
from .models import Diamond 

class DiamondSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Diamond
        fields = ('id', 'carat', 'clarity', 'cut', 'color', 'depth', 'table')
