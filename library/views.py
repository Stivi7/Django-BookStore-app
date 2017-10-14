from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
# Create your views here.

def index(request):
    books = Book.objects.all()[:10]
    author = Author.objects.all()
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'library/home.html', context)


def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'library/books.html', context)

def author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'library/authors.html', context)

def publisher(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers': publishers
    }
    return render(request, 'library/publishers.html', context)


#Detail views
def author_details(request, author_id):
    authorDetails = get_object_or_404(Author, pk=author_id)
    context = {
        'authorDetails': authorDetails
    }
    return render(request, 'details/authorDetails.html', context)

def publisher_details(request, pub_id):
    publisherDetails = get_object_or_404(Publisher, pk=pub_id)
    context = {
        'publisherDetails': publisherDetails
    }
    return render(request, 'details/pubDetails.html', context)

