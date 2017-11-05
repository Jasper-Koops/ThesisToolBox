from django.db import models
from person_tracker.models import Person
from notes.models import Note


class Book(models.Model):
    SOURCE_TYPE_CHOICES = (
        ('PRI', 'Primary'),
        ('SEC', 'Secondary')
    )
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    source_type = models.CharField(max_length=3, choices=SOURCE_TYPE_CHOICES, default='SEC')
    notes = models.ForeignKey(Note, blank=True, null=True)


class Pamphlet(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = models.ForeignKey(Note, blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = models.ForeignKey(Note, blank=True, null=True)

