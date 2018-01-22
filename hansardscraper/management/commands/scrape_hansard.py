from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup as Soup
import requests
import time
import random
from datetime import datetime
from hansardscraper.models import URL, Session, Debate, BlockQuote, Speaker


class Command(BaseCommand):
    help = "Scrapes hansard for new data."
    """
    This class needs a large try / except loop, which logs the except when its triggered. 
    """

    def get_html(self, url):
        # Mask session detail to avoid detection
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkit 537.36 (KHTML, like Gecko) Chrome",
            "Accept": "text/html, application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
        tries = 0
        while tries < 3:
            try:
                html = session.get(url, headers=headers)
                soup_output = Soup(html.text, "lxml")
                return soup_output

            except ConnectionError:
                tries += 1
                time.sleep(2)

        if tries == 3:
            raise ConnectionError('Connection failure!')


    def check_404(self, html):
        """
        Takes a html page and returns 'True' if its a 404 error page
        """
        title = html.select('.title')[0].text
        if title == 'Page not found':
            return True
        else:
            return False


    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('number', nargs='+', type=int)


    def handle(self, *args, **options):

        base_url = 'http://hansard.millbanksystems.com'

        self.stdout.write(self.style.SUCCESS('Starting scraping operation'))
        #Iterate over unchecked URLs
        unchecked_urls = URL.objects.filter(checked=False)

        counter = 0
        threshold = 99999999
        if options['number']:
            threshold = int(options['number'][0])
        for object in unchecked_urls:
            if counter >= threshold:
                break

            url = object.url
            time.sleep(random.randint(20,86))

            self.stdout.write(self.style.SUCCESS('Scraping %s') % url)

            #First check if the object exists, if not - attempt to visit the page
            try:
                Session.objects.get(url=url)
                pass

            except Session.DoesNotExist:
                #Check if page exists
                html = self.get_html(url)
                if self.check_404(html):
                    #404, skipp!
                    pass

                else:
                    #Get type from url
                    split = url.split('/')
                    type = split[3]
                    if type == 'commons':
                        type = 'com'
                    elif type == 'lords':
                        type = 'lrd'

                    #Get date from url
                    date = '-'.join([split[4], split[5], split[6]])
                    date = datetime.strptime(date, '%Y-%b-%d')
                    session_object = Session.objects.create(type=type, date=date, url=url)

                    #generate debate url list
                    debate_links = []
                    prev_url = ''
                    header_title = ''
                    for link in html.find_all('li', {'class': ['section-line']}):
                        # check if its just an header
                        headerobject = link.find('span', {'class': 'blank-section'})
                        if headerobject:
                            header_title = headerobject.a.text.strip() + ' '
                        else:
                            # Get title and url, add to list
                            title = header_title + link.a.text.strip()
                            url = base_url + link.a.attrs['href'].strip()
                            if url != prev_url:
                                debate_links.append((title, url))


                    for link in debate_links:
                        title = link[0]
                        debate_url = link[1]

                        #Check if debate object already exists, create if not
                        try:
                            debate_object = Debate.objects.get(
                                session=session_object,
                                url=debate_url,
                                title=title
                            )
                            pass
                        except Debate.DoesNotExist:

                            debate_object = Debate.objects.create(
                                session=session_object,
                                url=debate_url,
                                title=title
                            )

                        #Get HTML
                        html = self.get_html(link[1])
                        #Parse over BlockQuotes and create objects for each

                        blockquotes = html.select('.member_contribution')
                        for quote in blockquotes:
                            #get author
                            author = quote.select('.author')[0]
                            author_name = author.text

                            # check if author has url
                            try:
                                authorurl = author.a.attrs['href'].strip()
                                authorurl = base_url + authorurl
                            except:
                                authorurl = ''

                            #Check if author already exists, create object if not
                            try:
                                speaker = Speaker.objects.get(name=author_name, url=authorurl)
                            except Speaker.DoesNotExist:
                                speaker = Speaker.objects.create(name=author_name, url=authorurl)


                            BlockQuote.objects.create(speaker=speaker, text=quote.text.strip(), debate=debate_object)


            #All debates have been scraped, or the page was a 404, check URL object.
            print(url)
            url_object = URL.objects.get(url=url)
            url_object.checked = True
            url_object.save()
            counter +=1



