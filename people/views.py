from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def person_list(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def person_new(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)