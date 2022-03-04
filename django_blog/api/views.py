from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Blog
from .serializers import BlogSerializer


@api_view(["GET"])
def get_blogposts(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_blogposts(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
