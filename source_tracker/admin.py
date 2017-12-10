from django.contrib import admin
from source_tracker.models import Source


class SourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Source, SourceAdmin)

