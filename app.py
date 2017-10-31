from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/upper/<words>')
def upper(words):
    return words.upper()


@app.route('/lower/<words>')
def lower(words):
    return words.lower()
