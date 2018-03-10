from celery import shared_task
from hansardscraper.models import BlockQuote, QueryParams, SearchQuery
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchRank, SearchVector
import datetime

@shared_task
def trisearch(query, weight):

    search = SearchQuery.objects.create(
        query=query
    )

    results = BlockQuote.objects.annotate(similarity=TrigramSimilarity('text', query)).filter(similarity__gt=weight)

    for result in results:
        QueryParams.objects.create(
            quote = result,
            query = search,
        )

    search.finished = True
    search.completed = datetime.now()
    search.save()