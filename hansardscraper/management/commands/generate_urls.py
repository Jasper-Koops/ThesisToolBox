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

        #if options = 'start_year'
        self.stdout.write(self.style.SUCCESS('Generating urls'))
        base_url = 'http://hansard.millbanksystems.com'
        years = ['18' + str(x) for x in range(60,71)]
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        types = ['commons', 'lords']

        counter = 0
        skipped = 0
        for year in years:
            for month in months:
                for type in types:
                    for day in range(1,32):
                        url = '/'.join([base_url, type, year, month, str(day)])
                        try:
                            url_object = URL.objects.get(url=url)
                            skipped +=1
                            counter +=1
                        except URL.DoesNotExist:
                            url_object = URL.objects.create(url=url)
                            counter +=1

        self.stdout.write(self.style.SUCCESS('Added %d URLS, skipped %d') % (counter, skipped))




#self.stdout.write(self.style.SUCCESS('Added %d phones to the database.') % counter)


#http://hansard.millbanksystems.com/commons/1844/jul/11/