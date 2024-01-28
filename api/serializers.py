from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.exceptions import ValidationError
from .models import  News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'description', 'author', 'heshtag')
    
    def validation(self, data):
        category = data.get(category, None)
        title = data.get(title, None)
        author = data.get(author, None)
        heshtag = data.get(heshtag, None)
    
        if title.isalpha():
            raise ValidationError(
                {
                    'status':False,
                    'message':"Yangiliklarning kategoriyasi yoki sarlavhasi harflardan tashkil topishi kerak"
                }
            )
        return data    