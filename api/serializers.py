from library.models import Author, Publisher, Book
from rest_framework import serializers

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name', 'author_address', 'birthday', 'phone_number', 'author_email')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('publisher_name', 'publisher_address', 'publisher_email', 'web')