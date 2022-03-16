from .models import Dog
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'age', 'weight']