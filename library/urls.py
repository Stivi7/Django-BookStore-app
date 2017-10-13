from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import index, books, author, publisher



urlpatterns = [
    #
    url(r'^$', views.index, name='index'),
    #books/
    url(r'^books/$', views.books, name='books'),
    #books/author/
    url(r'^books/author/$', views.author, name='author'),
    #books/author/publisher
    url(r'^books/author/publisher$', views.publisher, name='publisher')
]