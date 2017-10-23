from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_address = models.CharField(max_length=200)
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=200)
    author_email = models.EmailField()

    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    publisher_address = models.CharField(max_length=200)
    publisher_email = models.EmailField()
    web = models.URLField()

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('library:books')

    def __str__(self):
        return self.title
    