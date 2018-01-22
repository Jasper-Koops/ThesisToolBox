from bs4 import BeautifulSoup as Soup
import requests

keywords = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
years = ['1861', '1862', '1863', '1864', '1865']
type = ['commons', 'lords']


#url = 'http://hansard.millbanksystems.com/commons/1844/jul/11/civil-disabilities-of-dissenters'

url = 'http://hansard.millbanksystems.com/lords/1861/feb/05/address-in-answer-to-her-majestys-speech'


def get_soup(url):
    """Uses spoofed headers on url, returns souped data"""
    # Mask session detail to avoid detection
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html, application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    html = session.get(url, headers=headers)
    soup_output = Soup(html.text, "lxml")
    return soup_output



html = get_soup(url)
#type UIT URL
#title = html.select('.title')[0].text
#date  -- UIT URL

blockquotes = html.select('.member_contribution')


for quote in blockquotes:
    author = quote.select('.author')[0]
    author_name = author.text
    #check if author has url
    try:
        authorurl = author.a.attrs['href'].strip()
        print(authorurl)
    except:
        print('no_url')
        authorurl = ''



# for quote in html.find_all('div', {'class': ['member_contribution']}):
#
#     author = quote.select('.author')
#     print(author[0])



#




# debate_links = []
# for link in html.find_all('span', {'class': [['minor-section', 'major-section']]}):
#     debate_links.append(link.a.attrs['href'].strip())
# print(debate_links)

#Pak blockquotes,
#haal sprekers eruit
#
# if title == 'Page not found':
#     print('YO DIT WERKT')
# print(title)

#Sessie
#Debat
#Blockquote