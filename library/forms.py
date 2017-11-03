from django import forms
from library.models import Author, Book, Publisher
from django.forms import ModelChoiceField
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'year', 'author', 'publisher']
    
    #override the fields
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('owner')
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(owner=self.request)
        self.fields['publisher'].queryset = Publisher.objects.filter(owner=self.request)
        

   