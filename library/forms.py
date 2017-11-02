from django import forms
from library.models import Author, Book, Publisher
from django.forms import ModelChoiceField
from django.contrib.auth.models import User

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    isbn = forms.CharField(max_length=200)
    year = forms.IntegerField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('owner')
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(owner=self.request)
        self.fields['publisher'].queryset = Publisher.objects.filter(owner=self.request)