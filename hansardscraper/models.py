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


class Search(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    finished = models.BooleanField(default=False)

    @property
    def query(self):
        if self.simple_query:
            return self.simple_query
        if self.query:
            return self.query

    def __str__(self):
        return 'search on ' + str(self.started)


class SimpleQuery(models.Model):
    search = models.ForeignKey(Search, related_name='simple_query')
    term = models.CharField(max_length=200)
    results = models.ManyToManyField(
        BlockQuote,
        through='SimpleQueryParams',
        blank=True
    )

    def __str__(self):
        return 'SimpleSearchQuery__' + str(self.search)


class Query(models.Model):
    search = models.ForeignKey(Search, related_name='query')
    terms = models.CharField(max_length=200)
    results = models.ManyToManyField(
        BlockQuote,
        through='QueryParams',
        blank=True
    )
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.terms)


class SimpleQueryParams(models.Model):
    quote = models.ForeignKey(BlockQuote)
    query = models.ForeignKey(SimpleQuery)
    created = models.DateTimeField(auto_now_add=True)


class QueryParams(models.Model):
    quote = models.ForeignKey(BlockQuote)
    query = models.ForeignKey(Query)
    matches = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
