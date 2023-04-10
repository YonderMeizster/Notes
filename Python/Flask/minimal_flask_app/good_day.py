from flask import Flask

# callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def good_day():
    return 'Good day!\n'
