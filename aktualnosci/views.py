from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blog_new(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)