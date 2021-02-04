from flask import Flask, request
from page_analyzer import ReviewScraper, Analyzer

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        print(request.json['url'])
        url = request.json['url']
    return {"res": "Success"}

@app.route('/hello')
def hello():
    return {'res': 'hello'}