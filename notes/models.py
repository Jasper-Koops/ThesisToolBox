from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db import models


class Tag(models.Model):
    added_on = models.DateTimeField(default=timezone.now, editable=True)
    name = models.CharField(max_length=300)
    notes = GenericRelation('Note', blank=True, null=True, related_name='notes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Note(models.Model):
    added_on = models.DateTimeField(default=timezone.now, editable=True)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    tags = models.ManyToManyField(Tag, blank=True, related_name='note_tags')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.content[:30]
