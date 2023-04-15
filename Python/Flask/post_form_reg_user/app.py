from flask import *
import json


with open('user_data/users', "w") as json_users:
    json_users.write("[]")


app = Flask(__name__)


id_count = 0


@app.get('/users/new')
def get_reg_form():
    return render_template('users/new_user.html')


@app.post('/users')
def reg_user():
    global id_count

    characterisic = request.form.to_dict()
    characterisic['id'] = id_count
    id_count += 1

    with open('user_data/users', "r") as json_users:
        users: list = json.loads(json_users.read())

    users.append(characterisic)

    with open('user_data/users', "w") as json_users:
        json_users.write(json.dumps(users))

    return redirect('/', 302)


@app.get('/')
def ind():
    with open('user_data/users', "r") as json_users:
        chars = json_users.read()

        try:
            users = json.loads(chars)
        except Exception:
            users = []

    return render_template('index.html', users=users)
