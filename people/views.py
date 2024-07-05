from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from azure.storage.blob import BlobServiceClient
import os
from azure.identity import ClientSecretCredential
from django.views.decorators.csrf import csrf_exempt
from azure.storage.blob import BlobServiceClient
from organization.models import Organization


from django.http import JsonResponse
from django.forms.models import model_to_dict

@api_view(["POST"])
@csrf_exempt
def person_new(request):
    data = request.data.copy()
    organization_id = data.pop("organization")[0]
    organization = get_object_or_404(Organization, pk=organization_id)
    photo = request.FILES["photo"]
    print(data)

    client_id = os.getenv("AZURE_CLIENT_ID")
    tenant_id = os.getenv("AZURE_TENANT_ID")
    client_secret = os.getenv("AZURE_CLIENT_SECRET")
    azure_storage_url = os.getenv("AZURE_STORAGE_URL")

    credentials = ClientSecretCredential(
        client_id=client_id, client_secret=client_secret, tenant_id=tenant_id
    )
    blob_service_client = BlobServiceClient(
        account_url=azure_storage_url, credential=credentials
    )

    container_name = "wspolnasprawaphotos"
    blob_name = photo.name
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    container_client = blob_service_client.get_container_client(container_name)

    photo_data = photo.read()
    blob_client.upload_blob(photo_data)
    blob_url = blob_client.url

    data.pop("photo", None)
    name = data.get('name')
    if isinstance(name, list):
        data['name'] = name[0]

    surname = data.get('surname')
    if isinstance(surname, list):
        data['surname'] = surname[0]

    description = data.get('description')
    if isinstance(description, list):
        data['description'] = description[0]

    person = Person(**data, organization=organization, photo_url=blob_url)
    person.save()

    return JsonResponse(model_to_dict(person), status=201)

@api_view(["GET"])
def person_list(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
