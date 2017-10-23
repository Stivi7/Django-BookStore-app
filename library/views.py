from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
from datetime import datetime
from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.http import is_safe_url
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    books = Book.objects.all()[:10]
    author = Author.objects.all()
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'library/home.html', context)

#Generic List views about, books, authors and publishers
class BookList(ListView):
    model = Book
    context_object_name = 'books'

class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'
    


#Detail views

class AuthorDetails(DetailView):
    model = Author
    template_name = 'details/authorDetails.html'
    
    
class PublisherDetails(DetailView):
    model = Publisher
    template_name = 'details/pubDetails.html'

#add an author
class AuthorCreate(CreateView):
    model = Author
    fields = ['author_name', 'author_address', 'birthday', 'phone_number', 'author_email']

#modify an author
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['author_name', 'author_address', 'birthday', 'phone_number', 'author_email']

#delete an author
def delete_a(request, author_id):
    if(request.method == 'DELETE'):
        try:
            a = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return JsonResponse({'deleted': False}) 
        a.delete()
        return JsonResponse({'deleted': True})


#adding a publisher
class PublisherCreate(CreateView):
    model = Publisher
    fields = ['publisher_name', 'publisher_address', 'publisher_email', 'web']


#modify a publisher
class PublisherUpdate(UpdateView):
    model = Publisher
    fields = ['publisher_name', 'publisher_address', 'publisher_email', 'web']

#delete a publisher
def delete_p(request, pub_id):
    if(request.method == 'DELETE'):
        try:
            p = Publisher.objects.get(pk=pub_id)
        except Publisher.DoesNotExist:
            return JsonResponse({'deleted': False})
        p.delete()
        return JsonResponse({'deleted': True})


#Add a new book (ModelView generic view)
class BookCreate(CreateView):
    model = Book
    fields = ['title', 'isbn', 'year', 'author', 'publisher']

#Modify a book
class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'isbn', 'year', 'author', 'publisher']

#Delete a book
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('library:books')








 



    



        
    

