from django.conf.urls import url, include
from django.contrib import admin
from . import views




urlpatterns = [
    #home/
    url(r'^$', views.headpage, name='headpage'),
    #home/latest
    url(r'^latest/$', views.index, name='index'),
    #home/books/
    url(r'^books/$', views.BookList.as_view(), name='books'),
    #home/author/
    url(r'^author/$', views.AuthorList.as_view(), name='author'),
    #home/publisher/
    url(r'^publisher/$', views.PublisherList.as_view(), name='publisher'),
    #home/author/id
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorDetails.as_view(), name='author_details'),
    #home/publisher/id
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetails.as_view(), name='publisher_details'),
    #home/books/id
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetails.as_view(), name='book_details'),
    #home/add
    url(r'^add$', views.AuthorCreate.as_view(), name="add"),
    #home/author/modify/id
    url(r'^author/modify/(?P<pk>[0-9]+)/$', views.AuthorUpdate.as_view(), name='modify'),
    #home/add_publisher
    url(r'^add_publisher$', views.PublisherCreate.as_view(), name="addpub"),
    #home/publisher/modify/id
    url(r'^publisher/modify/(?P<pk>[0-9]+)/$', views.PublisherUpdate.as_view(), name='modify_pub'),
    #home/author/delete/id
    url(r'^author/delete/(?P<author_id>[0-9]+)/$', views.delete_a, name='delete_a'),
    #home/publisher/delete/id
    url(r'^publisher/delete/(?P<pub_id>[0-9]+)/$', views.delete_p, name='delete_p'),
    #home/add_books
    url(r'^add_books$', views.BookCreate.as_view(), name='book-add'),
    #home/update_books/id
    url(r'^update_books/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),
    #home/delete_books/id
    url(r'^delete_books/(?P<pk>[0-9]+)/$', views.BookDelete.as_view(), name='book-delete'),
    #home/search
    url(r'^search/$', views.search_results, name="search_results")
]