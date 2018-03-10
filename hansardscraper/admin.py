from django.contrib import admin
from hansardscraper.models import *

class URLAdmin(admin.ModelAdmin):
    list_display = ['url', 'checked']
    list_filter = ['checked']


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name']


class SessionAdmin(admin.ModelAdmin):
    list_display = ['date', 'type', 'url']
    list_filter = ['type']


class DebateAdmin(admin.ModelAdmin):
    list_display = ['title', 'session', 'url']
    raw_id_fields = ['session']
    search_fields = ['title']


class BlockQuoteAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'debate']
    raw_id_fields = ['speaker', 'debate']
    search_fields = ['speaker__name', 'debate__title', 'text']


class SearchAdmin(admin.ModelAdmin):
    list_display = ['started', 'completed', 'finished']
    list_filter = ['finished']


class QueryAdmin(admin.ModelAdmin):
    list_display = ['search', 'terms', 'started', 'completed', 'finished']
    search_fields = ['query']


class SimpleQueryAdmin(admin.ModelAdmin):
    pass

class QueryParamAdmin(admin.ModelAdmin):
    list_display = ['query', 'quote', 'matches', 'created']
    search_fields = ['query', 'quote']
    list_filter = ['query']


admin.site.register(URL, URLAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Debate, DebateAdmin)
admin.site.register(BlockQuote, BlockQuoteAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(SimpleQuery, SimpleQueryAdmin)
admin.site.register(QueryParams, QueryParamAdmin)