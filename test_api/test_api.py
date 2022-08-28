import requests

base_url = 'https://reqres.in/api/'


def test_register():
    response = requests.post(base_url + 'register', json={
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    })

    assert response.status_code == 200
    assert int(response.json()['id']) == 4


def test_login():
    response = requests.post(base_url + 'login', json={
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    })

    assert response.status_code == 200
    assert str(response.json()['token']) == 'QpwL5tke4Pnpja7X4'


def test_create():
    response = requests.post(base_url + 'users', json={
        'name': 'Anna',
        'job': 'QA'
    })
    assert response.status_code == 201
    assert str(response.json()['name']) == 'Anna'
    assert str(response.json()['job']) == 'QA'
    global r_id
    r_id = response.json()['id']


def test_update():
    response = requests.put(base_url + 'users/' + r_id, json={
        'name': 'Nina',
        'job': 'QA Auto'
    })

    assert response.status_code == 200
    assert str(response.json()['name']) == 'Nina'
    assert str(response.json()['job']) == 'QA Auto'


def test_delete():
    response = requests.delete(base_url + 'users/' + r_id)

    assert response.status_code == 204

