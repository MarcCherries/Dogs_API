from telnetlib import DO
from webbrowser import get
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DogSerializer 
from .models import Dog 
from rest_framework import status
from django.shortcuts import get_object_or_404

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def dog_detail(request, pk):
    if request.method == 'GET':
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    elif request.method == 'PUT':
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
