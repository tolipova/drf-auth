from .models import *
from .serializers import *
from rest_framework import generics

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
