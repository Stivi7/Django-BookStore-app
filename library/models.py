from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_address = models.CharField(max_length=200)
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=200)
    author_email = models.EmailField()
    owner = models.ForeignKey('auth.User', related_name='authors', on_delete=models.CASCADE)
  

    def __str__(self):
        return self.author_name

    def get_absolute_url(self):
        return reverse('library:author')


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)
    publisher_address = models.CharField(max_length=200)
    publisher_email = models.EmailField()
    web = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='publishers', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.publisher_name

    def get_absolute_url(self):
        return reverse('library:publisher')


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
   

    def get_absolute_url(self):
        return reverse('library:books')

    def __str__(self):
        return self.title
    