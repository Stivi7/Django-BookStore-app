from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
from datetime import datetime
from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.utils.http import is_safe_url
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelChoiceField
from library.forms import BookForm
from django.contrib.postgres.search import SearchVector


#top 10 books in the home page
@login_required
def index(request):
    books = Book.objects.filter(owner=request.user)
    author = Author.objects.all()
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'library/home.html', context)

#Generic List views about, books, authors and publishers
class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    #shows only user's books
    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class AuthorList(LoginRequiredMixin, ListView):
    model = Author
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.filter(owner=self.request.user)
    
class PublisherList(LoginRequiredMixin, ListView):
    model = Publisher
    context_object_name = 'publishers'

    def get_queryset(self):
        return Publisher.objects.filter(owner=self.request.user)
    


#Detail views

class AuthorDetails(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'details/authorDetails.html'
    
    
class PublisherDetails(LoginRequiredMixin, DetailView):
    model = Publisher
    template_name = 'details/pubDetails.html'


class BookDetails(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'details/bookDetails.html'    

#Add an author
class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['author_name', 'author_address', 'birthday', 'phone_number', 'author_email']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AuthorCreate, self).form_valid(form)
    
    
#Modify an author
class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['author_name', 'author_address', 'birthday', 'phone_number', 'author_email']

#Delete an author
@login_required
def delete_a(request, author_id):
    if(request.method == 'DELETE'):
        try:
            a = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return JsonResponse({'deleted': False}) 
        a.delete()
        return JsonResponse({'deleted': True})


#Add a publisher
class PublisherCreate(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = ['publisher_name', 'publisher_address', 'publisher_email', 'web']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PublisherCreate, self).form_valid(form)


#Modify a publisher
class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = ['publisher_name', 'publisher_address', 'publisher_email', 'web']

#Delete a publisher
@login_required
def delete_p(request, pub_id):
    if(request.method == 'DELETE'):
        try:
            p = Publisher.objects.get(pk=pub_id)
        except Publisher.DoesNotExist:
            return JsonResponse({'deleted': False})
        p.delete()
        return JsonResponse({'deleted': True})


#Add a new book (ModelView generic view)
class BookCreate(LoginRequiredMixin, CreateView):
    template_name = 'library/book_form.html'
    form_class = BookForm

    #pass the self.request.user to the form
    def get_form_kwargs(self):
        kwargs = super(BookCreate, self).get_form_kwargs()
        kwargs.update({'owner': self.request.user})
        return kwargs
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate, self).form_valid(form)

    

    
#Modify a book
class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'isbn', 'year', 'author', 'publisher', 'book_cover']

#Delete a book
class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('library:books')

#render frontpage of authentication
def headpage(request):
    return render(request, 'library/headpage.html')

#signup
def signup(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('library:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


#Custom error views

def handler404(request):
    render(request, 'errors/404.html', status=404)


#search

def search_results(request):
    result = request.GET['search']
    search_res = Entry.objects.annotate(
        search=SearchVector('title', 'author', 'publisher'),
    ).filter(search=result)

    context = {
        'results': search_res
    }
    return render(request, 'library/search.html', context)









 



    



        
    

