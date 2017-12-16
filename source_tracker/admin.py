from django.contrib import admin
from source_tracker.models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'publication_date',
        'source_type',
        'added_on'
    ]
    list_filter = ['source_type', 'read']


admin.site.register(Source, SourceAdmin)

