from server.page_analyzer.Analyzer import Analyzer
from server.page_analyzer.ReviewScraper import ReviewScraper
from flask import Flask, request
import os

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')

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
            "time_taken": review_scraper.time,
            "score": analyzer.score,
        }
    return {"res": "default"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 5000))