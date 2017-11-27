from django.contrib import admin
from source_tracker.models import Book, Pamphlet, Article, ReactBook


class BookAdmin(admin.ModelAdmin):
    pass

class PamphletAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

class ReactBookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Pamphlet, PamphletAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.register(ReactBook, ReactBookAdmin)
