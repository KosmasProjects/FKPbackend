from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from .models import Blog
from django.http import JsonResponse
from django.forms.models import model_to_dict
from azure.storage.blob import BlobServiceClient
import os
from azure.identity import ClientSecretCredential
from django.views.decorators.csrf import csrf_exempt
from organization.models import Organization


@api_view(["POST"])
@csrf_exempt
def blog_new(request):
    data = request.data.copy()
    image = request.FILES["image"]

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
    blob_name = image.name
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    image_data = image.read()
    blob_client.upload_blob(image_data)
    blob_url = blob_client.url

    data.pop("image", None)
    title = data.get("title")
    if isinstance(title, list):
        data["title"] = title[0]

    description = data.get("description")
    if isinstance(description, list):
        data["description"] = description[0]

    author = data.get("author")
    if isinstance(author, list):
        data["author"] = author[0]

    blog = Blog(**data, image=blob_url)
    blog.save()

    return JsonResponse(model_to_dict(blog), status=201)


# @api_view(["POST"])
# @csrf_exempt
# def blog_new(request):
#     data = request.data.copy()
#     image = request.FILES["image"]

#     client_id = os.getenv("AZURE_CLIENT_ID")
#     tenant_id = os.getenv("AZURE_TENANT_ID")
#     client_secret = os.getenv("AZURE_CLIENT_SECRET")
#     azure_storage_url = os.getenv("AZURE_STORAGE_URL")

#     credentials = ClientSecretCredential(
#         client_id=client_id, client_secret=client_secret, tenant_id=tenant_id
#     )
#     blob_service_client = BlobServiceClient(
#         account_url=azure_storage_url, credential=credentials
#     )

#     container_name = "wspolnasprawaphotos"
#     blob_name = image.name
#     blob_client = blob_service_client.get_blob_client(container_name, blob_name)

#     image_data = image.read()
#     blob_client.upload_blob(image_data)
#     blob_url = blob_client.url

#     data.pop("image", None)
#     title = data.get('title')
#     if isinstance(title, list):
#         data['title'] = title[0]

#     description = data.get('description')
#     if isinstance(description, list):
#         data['description'] = description[0]

#     author = data.get('author')
#     if isinstance(author, list):
#         data['author'] = author[0]

#     blog = Blog(**data, image=blob_url)
#     blog.save()

#     return JsonResponse(model_to_dict(blog), status=201)


@api_view(["GET"])
def blog_list_fundacja_kochania_poznania(request):
    blogs = Blog.objects.filter(fundacja_kochania_poznania=True).order_by(
        "-date", "-id"
    )
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog_list_pomniki_poznania(request):
    blogs = Blog.objects.filter(pomniki_poznania=True).order_by("-date", "-id")
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog_list_wspolna_sprawa(request):
    blogs = Blog.objects.filter(wspolna_sprawa=True).order_by("-date", "-id")
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog_list_cieliczko_pl(request):
    blogs = Blog.objects.filter(cieliczko_pl=True).order_by("-date", "-id")
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog_list_poznanskie_legendy(request):
    blogs = Blog.objects.filter(poznanskie_legendy=True).order_by("-date", "-id")
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def blog_new(request):
#     serializer = BlogSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    data = request.data.copy()

    if "image" in request.FILES:
        image = request.FILES["image"]

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
        blob_name = image.name
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)

        image_data = image.read()
        blob_client.upload_blob(image_data)
        blob_url = blob_client.url

        data.pop("image", None)
        data["image"] = blob_url

    serializer = BlogSerializer(blog, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["PUT"])
# # @permission_classes([IsAuthenticated])
# def blog_edit(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     serializer = BlogSerializer(blog, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
