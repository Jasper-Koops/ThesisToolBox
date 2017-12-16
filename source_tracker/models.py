from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from person_tracker.models import Person
from notes.models import Note, Tag

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Source(models.Model):
    SOURCE_TYPE_CHOICES = (
        ('PRI', 'Primary'),
        ('SEC', 'Secondary')
    )

    SOURCE_CLASS_CHOICES = (
        ('BO', 'Book'),
        ('AR', 'Article')
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person)
    publication_date = models.DateField()
    added_on = models.DateTimeField(default=timezone.now, editable=True)
    source_type = models.CharField(max_length=3, choices=SOURCE_TYPE_CHOICES, default='SEC')
    source_class = models.CharField(max_length=3, choices=SOURCE_CLASS_CHOICES, default='BO')
    publisher_name = models.CharField(max_length=255)
    publisher_city = models.CharField(max_length=255)
    notes = GenericRelation(Note, blank=True, null=True, related_name='notes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='source_tags')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
