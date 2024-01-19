from rest_framework import serializers
from .models import NewsCategory, News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'description', 'author', 'heshtag')