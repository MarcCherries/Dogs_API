from telnetlib import DO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DogSerializer 
from .models import Dog 
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def dogs_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)