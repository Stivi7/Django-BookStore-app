from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
# Create your views here.

def index(request):
    books = Book.objects.all()[:10]
    context = {
        'books': books,
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


##Detail views
def adetails(request, id):
    authorDetails = Author.objects.get(pk=id)
    context = {
        'authorDetails': authorDetails
    }
    return render(request, 'library/authorDetails.html', context)

