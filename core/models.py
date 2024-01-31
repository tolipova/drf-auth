from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_price = models.IntegerField()
    book_isbn = models.IntegerField()
    image_url = models.CharField(max_length=255)