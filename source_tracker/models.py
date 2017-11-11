from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from person_tracker.models import Person
from notes.models import Note

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


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
    publisher_name = models.CharField(max_length=255)
    publisher_city = models.CharField(max_length=255)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')


class Pamphlet(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')

