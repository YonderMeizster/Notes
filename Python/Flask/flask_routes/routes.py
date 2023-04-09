from flask import Flask


app = Flask(__name__)


@app.post('/')
def get_hello():

    return 'Hello!\n'

app.run(port=8000)