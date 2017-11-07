"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from library import views
from rest_framework import routers
from api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


#api router
router = routers.DefaultRouter()
router.register(r'authors', api_views.AuthorViewSet)
router.register(r'books', api_views.BookViewSet)
router.register(r'publishers', api_views.PublisherViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('library.urls', namespace='library')),
    url(r'^', include('library.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # api routes
    url(r'^api/', include(router.urls)),
    url(r'^users/$', api_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', api_views.UserDetail.as_view()),
    url(r'^get-token/', obtain_auth_token),
    url(r'^authordetail/(?P<pk>[0-9]+)/$', api_views.AuthorDetail.as_view(), name='author-detail'),
    url(r'^bookdetail/(?P<pk>[0-9]+)/$', api_views.BookDetail.as_view(), name='book-detail'),
    url(r'^publisherdetail/(?P<pk>[0-9]+)/$', api_views.PublisherDetail.as_view(), name='publisher-detail')
]

handler404 = views.handler404

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)