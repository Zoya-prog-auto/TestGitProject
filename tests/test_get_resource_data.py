import httpx
from jsonschema import validate
import allure
from core.contracts import RESOURCE_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCES = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение списка ресурсов')

def test_list_resources():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + LIST_RESOURCES}'):
        response = httpx.get(BASE_URL + LIST_RESOURCES)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEME)
            with allure.step('Проверяем начало поля Color'):
                assert item['color'].startswith('#')

def test_single_resource():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    validate(data, RESOURCE_DATA_SCHEME)
    with allure.step('Проверяем начало поля Color'):
        assert data['color'].startswith('#')

def test_resource_not_found():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + NOT_FOUND_RESOURCE}'):
        response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404