from flask import Flask, render_template


app = Flask(__name__)


@app.route('/users/<id>')
def users(id):
    return render_template('index.html', id=id)


l = ['Элемент 0', 'Элемент 1', 'Элемент 2', 'Элемент N']


@app.route('/list')
def list():
    return render_template('list.html', l=l)
