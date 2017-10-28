from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from api.serializers import AuthorSerializer, BookSerializer, PublisherSerializer, UserSerializer
from library.models import Author, Book, Publisher
from rest_framework import permissions
from django.contrib.auth.models import User

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    #creates an owner field for the serializers to use
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
