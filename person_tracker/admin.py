from django.contrib import admin
from person_tracker.models import Nationality, Person
# Register your models here.

class NationalityAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'nationality', 'branch']

    def full_name(self, obj):
        return obj.full_name
    list_filter = ['historian']

admin.site.register(Nationality, NationalityAdmin)
admin.site.register(Person, PersonAdmin)
