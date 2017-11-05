from django.contrib import admin
from person_tracker.models import Nationality, Person
# Register your models here.

class NationalityAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Nationality, NationalityAdmin)
admin.site.register(Person, PersonAdmin)
