from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import index, books, author, publisher



urlpatterns = [
    #home/
    url(r'^$', views.index, name='index'),
    #home/books/
    url(r'^books/$', views.books, name='books'),
    #home/author/
    url(r'^author/$', views.author, name='author'),
    #home/publisher/
    url(r'^publisher/$', views.publisher, name='publisher'),
    #home/author/id
    url(r'^author/(?P<id>\w{0,50})/$', views.adetails, name='adetails')
]