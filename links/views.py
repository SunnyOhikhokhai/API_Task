from django.shortcuts import render
from rest_framework import generics
from .models import Link
from .serizliers import LinkSerializer


# Create your views here.

class PostListApi(generics.ListAPIView):
    model = Link
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    model = Link
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
