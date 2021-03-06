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
    url('^tags/$', TagOverview.as_view(), name='tag_overview'),
    url('^tag/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name='tag_detail'),
    url('^tags/create/$', TagCreate.as_view(), name='tag_create'),

    url('^todo/$', TodoView.as_view(), name='todo'),

    url('^create-note/(?P<model>[a-zA-Z]+)/(?P<app>[a-zA-Z_]+)/(?P<model_pk>[0-9]+)/$', TagNoteAdd.as_view(), name='tag_create_note'),
    url('^(?P<pk>[0-9]+)/$', NoteDetail.as_view(), name='note-detail'),
    url('^(?P<pk>[0-9]+)/update/$', NoteUpdateView.as_view(), name='tag_note_update'),

]


