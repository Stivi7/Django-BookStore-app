from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import AuthorSerializer, BookSerializer, PublisherSerializer
from library.models import Author, Book, Publisher


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
