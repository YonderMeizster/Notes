from flask import Flask, request, render_template


app = Flask(__name__)
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def get_users():
    part = request.args.get('name')
    applied_users = []
    if part is not None:
        applied_users = [user for user in users if part in user]
    return render_template('/users/index.html', users=applied_users)


@app.route('/users/<input>')
def get_input(input):
    return input


app.run(port=5000)
