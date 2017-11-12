from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    added_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Note(models.Model):
    added_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    tags = models.ManyToManyField(Tag, blank=True)
