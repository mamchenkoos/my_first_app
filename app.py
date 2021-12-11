import json
from flask import Flask, request
from middleware.auth import AuthorizationMiddle

app = Flask(__name__)
app.wsgi_app = AuthorizationMiddle(app.wsgi_app)


users = {
    '1': {'name': 'admin', 'money': 100500},
    '2': {'name': 'ivan_1', 'money': 0},
    '3': {'name': 'ivan_2', 'money': 100}
}


@app.route('/')
def index():
    print('I am from index')
    return 'Hello'


@app.route('/get-money')
def get_money():
    user_id = request.headers.get('auth_middleware_user')
    return json.dumps({'user_id': user_id, 'money': users.get(user_id)['money']})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)