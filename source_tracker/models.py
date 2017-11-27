from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from person_tracker.models import Person
from notes.models import Note, Tag

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


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
    tags = models.ManyToManyField(Tag, blank=True, related_name='book_tags')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class ReactBook(models.Model):
    SOURCE_TYPE_CHOICES = (
        ('PRI', 'Primary'),
        ('SEC', 'Secondary')
    )
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    source_type = models.CharField(max_length=3, choices=SOURCE_TYPE_CHOICES, default='SEC')
    publisher_name = models.CharField(max_length=255)
    publisher_city = models.CharField(max_length=255)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)




class Pamphlet(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='pamphlet_tags')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(auto_now=True)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='article_tags')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

