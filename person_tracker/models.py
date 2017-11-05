from django.db import models
from notes.models import Note
# Create your models here.

class Nationality(models.Model):
    name = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=255)
    added_on = models.DateField(auto_now=True)
    year_of_birth = models.DateField()
    year_of_death = models.DateField(blank=True)
    nationality = models.ForeignKey(Nationality, blank=True)
    branch = models.CharField(max_length=255)
    notes = models.ForeignKey(Note, blank=True, null=True)