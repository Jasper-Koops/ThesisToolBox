from django.db import models

class URL(models.Model):
    url = models.URLField()
    checked = models.BooleanField(default=False)


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    TYPE_CHOICES = (
        ('com', 'house of commons'),
        ('lrd', 'house of lords'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=3)
    date = models.DateTimeField()
    url = models.URLField()


class Debate(models.Model):
    session = models.ForeignKey(Session)
    title = models.CharField(max_length=400)
    url = models.URLField()


class BlockQuote(models.Model):
    debate = models.ForeignKey(Debate)
    speaker = models.ForeignKey(Speaker)
    text = models.TextField()


