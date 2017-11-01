from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    isbn = forms.CharField(max_length=200)
    year = forms.IntegerField(null=True)
    author = forms.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = forms.ForeignKey(Publisher, on_delete=models.CASCADE)
    

