from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import IsAuthorOrReadOnly

# Create your views here.

class NewsListCreateViewApi(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class NewsUpdateOrDeleteViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers