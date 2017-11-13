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
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', Home.as_view(), name='source_tracker_home'),
    url('^book-create/', BookCreate.as_view(), name='book_create'),
    url('^books/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book_detail'),
    url('^pamphlet-create/', PamphletCreate.as_view(), name='pamphlet_create'),
    url('^pamphlets/(?P<pk>[0-9]+)/$', PamphletDetail.as_view(), name='pamphlet_detail'),
    url('^article-create/', ArticleCreate.as_view(), name='article_create'),
    url('^articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view(), name='article_detail'),
    url('^create_note/(?P<model>[a-zA-Z]+)/(?P<app>[a-zA-Z_]+)/(?P<model_pk>[0-9]+)/$', SourceNoteAdd.as_view(), name='source_create_note'),
]
