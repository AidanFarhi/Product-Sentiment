from server.page_analyzer.Analyzer import Analyzer
from server.page_analyzer.ReviewScraper import ReviewScraper
from flask import Flask, request
import os
import requests
from lxml.html import fromstring
from random import choice

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

# Global variables
GLOBAL_PROXY = ''  # This will be set once the front end Main() is loaded
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
]
SESSION_AGENT = ''  #This will be set once the front end Main() is loaded

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# This route will be hit once Main() is first loaded
# It sets the proxy IP and User-Agent for the session
@app.route('/set-session', methods=['GET'])
def set_session():
    # First get a list of proxies from web
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    
    print(proxies)
    # Now test them and set one that works
    url = 'https://httpbin.org/ip'
    for proxy in proxies:
        try:
            res = requests.get(url, proxies={'http': proxy, 'https': proxy})
            print(res)
            if res.ok:
                GLOBAL_PROXY = proxy
                break
        except:
            print('Error, proxy not valid')
    
    # Now set the User-Agent for the session
    SESSION_AGENT = choice(USER_AGENTS)
    return {"Proxy": GLOBAL_PROXY, "Session-User-Agent": SESSION_AGENT}

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        url = request.json['url']
        review_scraper = ReviewScraper(url, GLOBAL_PROXY, SESSION_AGENT)
        reviews = review_scraper.get_reviews()
        analyzer = Analyzer(reviews)
        analyzer.analyze_reviews()
        return {
            "positive_hits": analyzer.total_positive_hits,
            "negative_hits": analyzer.total_negative_hits,
            "reviews_scraped": review_scraper.reviews_scraped,
            "time_taken": review_scraper.time,
            "score": analyzer.score,
        }
    return {"res": "default"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 5000))