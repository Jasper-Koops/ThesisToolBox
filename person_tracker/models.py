from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from notes.models import Note, Tag
# Create your models here.

class Nationality(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "nationalities"

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
    notes = GenericRelation(Note, null=True, blank=True, related_query_name='notes')
    tags = models.ManyToManyField(Tag, blank=True)

    @property
    def full_name(self):
        return self.firstname + " " + self.middlename + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.middlename + " " + self.lastname