from django.db import models
from fuzzywuzzy import fuzz


class URL(models.Model):
    url = models.URLField()
    checked = models.BooleanField(default=False)


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)

    @property
    def debates(self):
        debates = Debate.objects.filter(quotes__in=self.quotes.all())
        return debates.distinct()

    @property
    def sessions(self):
        sessions = Session.objects.filter(debates__in=self.debates)
        return sessions.distinct()

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

    @property
    def speakers(self):
        linked_quotes = BlockQuote.objects.filter(debate__in=self.debates.all())
        speakers = Speaker.objects.filter(quotes__in=linked_quotes)
        return speakers.distinct()

    def __str__(self):
        return ("session on %s" % (self.date))


class Debate(models.Model):
    session = models.ForeignKey(Session, related_name='debates')
    title = models.CharField(max_length=400)
    url = models.URLField()

    @property
    def speakers(self):
        speakers = Speaker.objects.filter(quotes__in=self.quotes.all())
        return speakers.distinct()

    def __str__(self):
        return self.title


class BlockQuote(models.Model):
    debate = models.ForeignKey(Debate, related_name='quotes')
    speaker = models.ForeignKey(Speaker, related_name='quotes')
    text = models.TextField()

    def __str__(self):
        return ("quote %d - %s" % (self.pk, self.debate.title))


class Search(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True)
    finished = models.BooleanField(default=False)

    @property
    def linked_query(self):
        """
        There can only be one
        At least, I hope - because it will crash otherwise
        """
        if self.primitive_query:
            return self.primitive_query.first()

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


class PrimitiveQuery(models.Model):
    search = models.ForeignKey(Search, related_name='primitive_query')
    term = models.CharField(max_length=200)

    def __str__(self):
        return 'PrimitiveSearchQuery__' + str(self.search)


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


class PrimitiveQueryResult(models.Model):
    quote = models.ForeignKey(BlockQuote)
    query = models.ForeignKey(PrimitiveQuery, related_name='results')
    created = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True, null=True)
    seen = models.BooleanField(default=False)
    usefull = models.NullBooleanField(blank=True, null=True, default=None)

    def __str__(self):
        return self.query.term + ' ' + str(self.quote.pk)

    def create_excerpt(self):
        """
        Creates excerpts from matches, for quick scanning
        :return: excerpts, with matching words capitalized
        """
        excerpts = ""
        query = self.query.term
        text = self.quote.text
        split_text = text.split()
        for word in split_text:
            if fuzz.ratio(word.lower(), query.lower()) > 88:
            # if word.lower() == query.lower():
                index = split_text.index(word)
                # Capitalize matched term, so its easier to read
                split_text[index] = word.upper()
                # Create excerpts
                excerpts += ' '.join(split_text[index -40: index + 40])
                excerpts += "\n\n=========\n\n"
        self.excerpt = excerpts
        self.save()