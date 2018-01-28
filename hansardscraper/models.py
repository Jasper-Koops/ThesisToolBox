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
    session = models.ForeignKey(Session, related_name='debates')
    title = models.CharField(max_length=400)
    url = models.URLField()

    def __str__(self):
        return self.title


class BlockQuote(models.Model):
    debate = models.ForeignKey(Debate, related_name='quotes')
    speaker = models.ForeignKey(Speaker, related_name='quotes')
    text = models.TextField()


class SearchQuery(models.Model):
    query = models.CharField(max_length=200)
    results = models.ManyToManyField(BlockQuote, through='QueryParams', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.query

    # @property
    # def get_debates(self):
    #     """
    #     This might be very slow!
    #     """
    #     # debate_list = []
    #     # for quote in self.quotes.all():
    #     #     if quote.debate not in debate_list:
    #     #         debate_list.append(quote.debate)
    #     # return debate_list
    #
    #     #This will most lickely crash
    #     return self.quotes.debate.distinct()

#
class QueryParams(models.Model):
    quote = models.ForeignKey(BlockQuote)
    query = models.ForeignKey(SearchQuery)
    matches = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)



