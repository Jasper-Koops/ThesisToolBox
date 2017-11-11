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
    url('^$', Home.as_view(), name='person_tracker_home'),
    url('^persons/$', PersonOverview.as_view(), name='person_overview'),
    url('^persons/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name='person_detail'),
    url('^add-person/', PersonCreate.as_view(), name='person_create'),
    url('^add-nationality/', NationalityCreate.as_view(), name='nationality_create'),
    url('^create_note/(?P<model>[a-zA-Z]+)/(?P<app>[a-zA-Z_]+)/(?P<model_pk>[0-9]+)/$', PersonNoteAdd.as_view(), name='person_create_note'),
]


