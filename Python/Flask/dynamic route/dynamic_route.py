from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Greetings!'


@app.route('/users/<user_id>')
def user_id(user_id):
    return f'User ID is {user_id}'


@app.route('/users/<user_id>/<rank_id>')
def id_rank(user_id, rank_id):
    return f'User ID is {user_id} and rank ID is {rank_id}'
