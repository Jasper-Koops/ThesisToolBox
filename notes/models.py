from django.db import models

# Create your models here.
class Note(models.Model):
    added_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
