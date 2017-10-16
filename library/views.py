from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
from datetime import datetime
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

def add(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        email = request.POST['email']

        author = Author(author_name=name, author_address=address, birthday=birthday, phone_number=phone, author_email=email)
        author.save()

        return redirect('/home/author')
    else:
        return render(request, 'forms/add_author.html')


def modify(request, author_id):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        email = request.POST['email']

        a = Author.objects.get(pk=author_id)
        

        a.author_name = name
        a.author_address = address
        a.birthday = birthday
        a.phone_number = phone
        a.author_email = email
        a.save()

        return redirect('/home/author')
    else:
        author = get_object_or_404(Author, pk=author_id)
        return render(request, 'forms/modify_author.html', {'author': author})

def addpub(request):
    if(request.method == 'POST'):
        p_name = request.POST['p_name']
        p_address = request.POST['p_address']
        p_email = request.POST['p_email']
        web = request.POST['web']

        publisher = Publisher(publisher_name=p_name, publisher_address=p_address, publisher_email=p_email, web=web)
        publisher.save()

        return redirect('/home/publisher')
    else:
        return render(request, 'forms/add_publisher.html')





