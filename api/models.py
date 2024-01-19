from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewsCategory(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
    
class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    heshtag = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title