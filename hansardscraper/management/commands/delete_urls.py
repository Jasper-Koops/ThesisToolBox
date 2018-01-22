from django.core.management.base import BaseCommand, CommandError
from hansardscraper.models import URL

#create url
#check if already in db, skipp if this is the case


class Command(BaseCommand):
    help = "Generates session URLS to be used"

    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument('start_year', nargs='+', type=int)
    #     parser.add_argument('end_year', nargs='+', type=int)


    def handle(self, *args, **options):
        total = URL.objects.all().count()
        URL.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted %d urls from the database') % total)