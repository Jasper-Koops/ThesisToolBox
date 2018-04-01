from celery import shared_task
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchRank, SearchVector
import datetime
from hansardscraper.models import BlockQuote, PrimitiveQueryResult, PrimitiveQuery, Search, QueryParams


@shared_task
def perform_query(text):
    current_search = Search.objects.create()
    vector = (SearchVector('text', weight='A') + SearchVector('debate__title', weight='B'))
    query = SearchQuery(text)
    search_results = BlockQuote.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.3).order_by('-rank')

    results = []

    # Create search query object
    search = PrimitiveQuery.objects.create(
        search=current_search,
        term=text
    )

    for search_result in search_results:
        result = PrimitiveQueryResult.objects.create(
            quote=search_result,
            query=search
        )
        result.create_excerpt()
        result.save()


    current_search.completed = datetime.datetime.now()
    current_search.finished = True
    current_search.save()


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