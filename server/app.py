from server.page_analyzer.Analyzer import Analyzer
from server.page_analyzer.ReviewScraper import ReviewScraper
from flask import Flask, request

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        url = request.json['url']
        review_scraper = ReviewScraper(url)
        reviews = review_scraper.get_reviews()
        analyzer = Analyzer(reviews)
        analyzer.analyze_reviews()
        return {
            "positive_hits": analyzer.total_positive_hits,
            "negative_hits": analyzer.total_negative_hits,
            "reviews_scraped": review_scraper.reviews_scraped,
            "time_taken": review_scraper.time
        }
    return {"res": "default"}

@app.route('/hello')
def hello():
    return {'res': 'hello'}