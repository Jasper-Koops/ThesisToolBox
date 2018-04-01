from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^searches/$',
        SearchListView.as_view(),
        name='search_overview'
        ),
    url('^searches/(?P<pk>[0-9]+)/$',
        SearchDetailView.as_view(),
        name='search_detail'
        ),
    url('^quote/(?P<pk>[0-9]+)/$',
        QuoteDetailView.as_view(),
        name='quote_detail'
        ),
    url('^debate/(?P<pk>[0-9]+)/$',
        DebateDetailView.as_view(),
        name='debate_detail'
        ),
    url('^session/(?P<pk>[0-9]+)/$',
        SessionDetailView.as_view(),
        name='session_detail'
        ),
    url('^speaker/(?P<pk>[0-9]+)/$',
        SpeakerDetailView.as_view(),
        name='speaker_detail'
        ),
]


