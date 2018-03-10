from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework import routers
from.views import *
from rest_api.views import *

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'tags', TagViewSet)
router.register(r'sources', SourceViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', Index.as_view(), name='index'),
    url('^sources/', include('source_tracker.urls', namespace='sourcetracker')),
    url('^persons/', include('person_tracker.urls', namespace='persontracker')),
    url('^notes/', include('notes.urls', namespace='notes')),
    url('^scraper/', include('hansardscraper.urls', namespace='scraper')),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/',include(router.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

