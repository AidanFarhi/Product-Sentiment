from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print('hello')
    return {'res': 'hello'}