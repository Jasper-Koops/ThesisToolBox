from django.contrib import admin
from hansardscraper.models import *

class URLAdmin(admin.ModelAdmin):
    list_display = ['url', 'checked']
    list_filter = ['checked']


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


class SessionAdmin(admin.ModelAdmin):
    list_display = ['date', 'type', 'url']
    list_filter = ['type']


class DebateAdmin(admin.ModelAdmin):
    list_display = ['title', 'session', 'url']


class BlockQuoteAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'debate']


admin.site.register(URL, URLAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Debate, DebateAdmin)
admin.site.register(BlockQuote, BlockQuoteAdmin)