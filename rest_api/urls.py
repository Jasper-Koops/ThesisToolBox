"""ThesisToolBox URL Configuration

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
from .views import *


urlpatterns = [
    url(r'^books/$', BookList.as_view(), name='api_book_list'),
    url(r'^books/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book-detail'),

    url(r'^articles/$', ArticleList.as_view(), name='api_article_list'),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view(), name='article-detail'),

    url(r'^pamphlets/$', PamphletList.as_view(), name='api_pamphlet_list'),
    url(r'^pamphlets/(?P<pk>[0-9]+)/$', PamphletDetail.as_view(), name='pamphlet-detail'),

    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
]
