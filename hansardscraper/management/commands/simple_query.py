from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchRank, SearchVector
from hansardscraper.models import URL, Session, Debate, BlockQuote, Speaker, SearchQuery, QueryParams


class Command(BaseCommand):
    help = "Searches the database for the given query."


    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('query', nargs='+', type=str)


    def handle(self, *args, **options):
        vector = SearchVector('text')
        query = SearchQuery(options['query'][0])
        self.stdout.write(self.style.SUCCESS('Starting search operation'))
        search_query = SearchQuery.objects.create(query=query)
        set = BlockQuote.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.85).order_by('-rank')
        # self.stdout.write(set)
        for result in set:
            param = QueryParams.objects.create(quote=result, query=search_query)
            param.save()
        # search_query.results=set
        # search_query.finished=True
        # search_query.save()
        self.stdout.write(self.style.SUCCESS('Finished!'))







