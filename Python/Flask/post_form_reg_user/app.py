from flask import *
import json


app = Flask(__name__)
with open('user_data/users', "w") as _:
    pass


id_count = 0


@app.get('/users/new')
def get_reg_form():
    return render_template('users/new_user.html')


@app.post('/users')
def reg_user():
    global id_count
    with open('user_data/users', "r+") as json_users:
        data = json_users.read()
        new_user = request.form.to_dict()

        if len(data) == 0:
            json_users.write(json.dumps(new_user))
            return redirect('/', 302)

        curr_users = json.loads(data)
        curr_users[id_count] = new_user
        id_count += 1
        json_users.write(json.dumps(curr_users))
    return redirect('/', 302)


@app.get('/')
def ind():
    with open('user_data/users', "r") as json_users:
        data = json_users.read()
        if len(data) == 0:
            return render_template('index.html', users=[])
        users = json.loads(data)
    return render_template('index.html', users=users)
