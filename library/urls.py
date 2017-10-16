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
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_details, name='author_details'),
    #home/publisher/id
    url(r'^publisher/(?P<pub_id>[0-9]+)/$', views.publisher_details, name='publisher_details'),
    #home/add
    url(r'^add$', views.add, name="add"),
    #home/author/modify/id
    url(r'^author/modify/(?P<author_id>[0-9]+)/$', views.modify, name='modify'),
    #home/add_publisher
    url(r'^add_publisher$', views.addpub, name="addpub"),
    #home/publisher/modify/id
    url(r'^publisher/modify/(?P<pub_id>[0-9]+)/$', views.modify_pub, name="modify_pub"),
    #home/author/delete/id
    url(r'^author/delete/(?P<author_id>[0-9]+)/$', views.delete_a, name='delete_a'),
]