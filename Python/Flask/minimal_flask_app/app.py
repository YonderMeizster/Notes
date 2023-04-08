from flask import Flask

# callable WSGI-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Good day!\n'