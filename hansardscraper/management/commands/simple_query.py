from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchRank, SearchVector
from hansardscraper.models import URL, Session, Debate, BlockQuote, Speaker, SearchQuery


class Command(BaseCommand):
    help = "Searches the database for the given query."


    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('query', nargs='+', type=str)


    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting search operation'))
        search_query = SearchQuery.objects.create(query=query)

        vector = SearchVector('text')
        query = options['query'][0]
        set = BlockQuote.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        search_query.results=set
        search_query.finished=True
        search_query.save()

        self.stdout.write(self.style.SUCCESS('Finished!'))







