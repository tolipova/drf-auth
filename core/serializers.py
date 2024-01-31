from rest_framework import serializers
from .models import *
from rest_framework.fields import empty

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'book_name', 'book_price','book_isbn', 'image_url',)