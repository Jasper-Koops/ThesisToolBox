from django.db import models
from notes.models import Note
# Create your models here.

class Nationality(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255)
    added_on = models.DateField(auto_now=True)
    year_of_birth = models.DateField()
    year_of_death = models.DateField(blank=True, null=True)
    nationality = models.ForeignKey(Nationality, blank=True, null=True)
    branch = models.CharField(max_length=255)
    notes = models.ForeignKey(Note, blank=True, null=True)

    @property
    def full_name(self):
        return self.firstname + " " + self.middlename + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.middlename + " " + self.lastname