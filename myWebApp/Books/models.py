from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publicationDate = models.DateField() 