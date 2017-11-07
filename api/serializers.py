from library.models import Author, Publisher, Book
from rest_framework import serializers
from django.contrib.auth.models import User

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Author
        fields = ('author_name', 'author_address', 'birthday', 'phone_number', 'author_email', 'owner')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Publisher
        fields = ('publisher_name', 'publisher_address', 'publisher_email', 'web', 'owner')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'year', 'author', 'publisher', 'book_cover', 'owner')


class UserSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    publishers = serializers.PrimaryKeyRelatedField(many=True, queryset=Publisher.objects.all())
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'authors', 'publishers', 'books')