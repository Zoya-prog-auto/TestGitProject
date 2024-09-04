import httpx
import pytest
import json
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME, REGISTRATION_FAILURE_SCHEME, SUCCESSFUL_LOGIN_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USER = "api/register"
LOGIN_USER = "api/login"

json_file = open('/Users/Home/PycharmProjects/TestPthonProject/core/new_users_data.json')
users_data = json.load(json_file)

@pytest.mark.parametrize('users_data',users_data)
def test_successful_register(users_data):
    headers = {'Content-type': 'application/json'}
    response = httpx.post(BASE_URL + REGISTER_USER, json=users_data, headers=headers)
    assert response.status_code == 200

    validate(response.json(), REGISTERED_USER_SCHEME)

def test_unsuccessful_register():
    body = {
        "email": "sydney@fife"
    }
    response = httpx.post(BASE_URL + REGISTER_USER)
    assert response.status_code == 400

    validate(response.json(), REGISTRATION_FAILURE_SCHEME)

json_file = open('/Users/Home/PycharmProjects/TestPthonProject/core/login_users_data.json')
login_data = json.load(json_file)

@pytest.mark.parametrize('login_data',login_data)
def test_successful_login(login_data):

    response = httpx.post(BASE_URL + LOGIN_USER, json=login_data)
    assert response.status_code == 200

    validate(response.json(), SUCCESSFUL_LOGIN_SCHEME)