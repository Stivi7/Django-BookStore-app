from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_address = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    author_email = models.CharField(max_length=200)


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    publisher_address = models.CharField(max_length=200)
    publisher_email = models.CharField(max_length=200)
    web = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    