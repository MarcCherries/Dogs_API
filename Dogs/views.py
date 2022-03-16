from telnetlib import DO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DogSerializer 
from .models import Dog

# Create your views here.

@api_view(['GET'])
def dogs_list(request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)