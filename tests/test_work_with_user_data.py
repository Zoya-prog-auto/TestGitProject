import httpx
import datetime
import allure
from jsonschema import validate
from core.contracts import CREATE_USER_SHEME, UPDATE_USER_SCHEME

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"
UPDATE_USER = "api/users/2"
DELETE_USER = "api/users/2"

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем создание пользователя')

def test_create_user_with_name_and_job():
    with allure.step('Отправляем тело запроса'):
        body = {
        "name": "morpheus",
        "job": "leader"
        }
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATE_USER_SHEME)
    with allure.step('Проверяем поле name'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем поле job'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем поле createdAt'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем создание пользователя без name')
def test_create_user_without_name():
    with allure.step('Отправляем тело запроса'):
        body = {

             "job": "leader"
        }
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATE_USER_SHEME)
    with allure.step('Проверяем поле job'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем поле createdAt'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем создание пользователя без job')
def test_create_user_without_job():
    with allure.step('Отправляем тело запроса'):
        body = {
        "name": "morpheus",

        }
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, CREATE_USER_SHEME)
    with allure.step('Проверяем поле name'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем поле createdAt'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем обновление данных пользователя с помощью запроса PUT')
def test_update_user_with_name_and_job():
    with allure.step('Отправляем тело запроса'):
        body = {
        "name": "morpheus",
        "job": "zion resident"
        }
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + UPDATE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T',' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, UPDATE_USER_SCHEME)
    with allure.step('Проверяем поле name'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем поле job'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем поле updatedAt'):
        assert update_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем обновление данных пользователя с помощью запроса PATCH')
def test_patch_user_with_name_and_job():
    with allure.step('Отправляем тело запроса'):
        body = {
             "name": "morpheus",
             "job": "zion resident"
         }
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + UPDATE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response_json, UPDATE_USER_SCHEME)
    with allure.step('Проверяем поле name'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем поле job'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем поле updatedAt'):
        assert update_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания и изменения данных пользователей')
@allure.title('Проверяем удаление данных пользователя')
def test_user_delete():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + DELETE_USER}'):
        response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204