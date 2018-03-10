from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^searches/$',
        SearchListView.as_view(),
        name='search_overview'
        ),
    # url('^searches/(?P<pk>[0-9]+)/$',
    #     SearchDetailView.as_view(),
    #     name='search_detail'
    #     ),
]


