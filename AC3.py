# pip install google-api-python-client

from contextlib import closing
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from googleapiclient.discovery import build
import pprint

app = Flask(__name__)

@app.route('/google', methods=['GET', 'POST'])
def reenviar():
    if request.method == "POST":
        api_key = "AIzaSyDZY4tCSmJPQ1KHKfYFTTfyK3spMBRzlo8"
        cse_key = "669745d1113150082"
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=request.form['google_search'], cx=cse_key, num= 10).execute()
        g.resultado = result
        return redirect(url_for('resultados'))
    return render_template('pesquisa.html')

@app.route('/resultados', methods=['GET', 'POST'])
def resultados():
    if request.method == "POST":
        api_key = "AIzaSyDZY4tCSmJPQ1KHKfYFTTfyK3spMBRzlo8"
        cse_key = "669745d1113150082"
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=request.form['google_search'], cx=cse_key, num= 10).execute()
        g.resultado = result
        return redirect(url_for('resultados'))
    return render_template('resultados.html')
if __name__ == '__main__':
    app.run()
'''
teste fail 1 
# pip install google
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
  
# to search
query = "abacaxi"
teste = search(query, tld="com.br", num=10, stop=10, pause=2)
print(teste)
for item in search(query, tld="com.br", num=10, stop=10, pause=2):
    print(item)
'''

'''
dando erro as vezes 
from googleapi import google
num_page = 1
search_results = google.search("abacate", num_page)
for result in search_results:
    print(result.link)
    print(result.name)
'''
'''
teste fail
from googleapiclient.discovery import build

my_api_key = "AIzaSyDZY4tCSmJPQ1KHKfYFTTfyK3spMBRzlo8"
my_cse_id = "669745d1113150082"

def google_search(search_term, api_key, cse_id, **kwargs):
      service = build("customsearch", "v1", developerKey=api_key)
      res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
      return res['items']

results= google_search("abacaxi",my_api_key,my_cse_id,num=10) 

for result in results:
      print(result["link"])
'''
'''
esse ta indo
import requests
from bs4 import BeautifulSoup
import random
import pprint
 
text = 'python'
q = text.replace(' ', '+')
url = 'https://google.com/search?q=' + q
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]
 
headers = {'user-agent': Agent}
r = requests.get(url, headers=headers)
 
soup = BeautifulSoup(r.text, 'lxml')
#pprint.pprint(soup)
for info in soup.find_all('cite'):
    print(info)
    print(info.text)
    print('#######')
'''

'''
import json
from urllib.parse import urlencode
import requests
import random
from lxml import etree

def do_it_yourself_advanced():
    """If you had to do it yourself"""
    domain = 'com'
    pages = 2
    payload = {
        'q': 'abacate', # Query.
        # You'd need to figure out how to generate this.
        'uule': 'w+CAIQICIGQnJhc2ls', # Location.
    }
    headers = {
        'User-Agent': random.choice(
            [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                'Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            ]
        )          
    }

    results = [] # Parsed results.

    for count in range(0, pages * 10, 10):
        payload['start'] = count # One page is equal to 10 google results.

        params = urlencode(payload)
        url = f'https://www.google.{domain}/search?{params}'
        proxies = {
            'https': 'http://<username>:<password>@<host>:<port>',
        }

        # Scrape.
        response = requests.get(url=url, headers=headers)

        # Parse.
        parser = etree.HTMLParser()
        tree = etree.fromstring(
            response.text,
            parser,
        )

        result_elements = tree.xpath(
            './/div['
            ' contains(@class, "ZINbbc") '
            ' and not(@style="display:none")'
            ']'
            '['
            ' descendant::div[@class="kCrYT"] '
            ' and not(descendant::*[@class="X7NTVe"])' # maps
            ' and not(descendant::*[contains(@class, "deIvCb")])' # stories
            ']',
        )

        for element in result_elements:
            results.append(
                {
                'url': element.xpath('.//a/@href')[0],
                'title': element.xpath('.//h3//text()')[0],
                'description': element.xpath(
                    './/div[contains(@class, "BNeawe")]//text()',
                )[-1],
                # Other fields you would want.
            }
        )

    with open('diy_parsed_result_advanced.json', 'w+') as f:
        f.write(json.dumps(results, indent=2))
        print(f)
do_it_yourself_advanced()
'''