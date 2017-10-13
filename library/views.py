from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    
    return render(request, 'library/home.html')


def books(request):
    return render(request, 'library/books.html')

def author(request):
    return render(request, 'library/authors.html')

def publisher(request):
    return render(request, 'library/publishers.html')

