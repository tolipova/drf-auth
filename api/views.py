from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import IsAuthorOrReadOnly

# Create your views here.

class NewsListCreateViewApi(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    filter_backends = [ DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category','author']
    search_fields = [ 'author', 'category']
    ordering_fileds = ['username', 'createds']
    
class NewsUpdateOrDeleteViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers