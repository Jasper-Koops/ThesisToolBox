from django.contrib import admin
from notes.models import Note, Tag
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)