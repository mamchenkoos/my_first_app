import json
import requests


def get_token(username, password):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'username': username, 'password': password})
    response = requests.post('http://127.0.0.1:5001/token', headers=headers, data=data)
    return response.text


def make_get_request(url, token):
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    return response.text


if __name__ == '__main__':
    token = get_token(username='admin', password='admin')
    print('Token', token)
    result = make_get_request('http://127.0.0.1:5001/get_money', token)
    print('Result', result)
