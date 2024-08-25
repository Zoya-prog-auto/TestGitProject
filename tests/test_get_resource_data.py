import httpx
from jsonschema import validate

from core.contracts import RESOURCE_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCES = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
NOT_FOUND_RESOURCE = "api/unknown/23"

def test_list_resources():
    response = httpx.get(BASE_URL + LIST_RESOURCES)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)
        assert item['color'].startswith('#')

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    validate(data, RESOURCE_DATA_SCHEME)
    assert data['color'].startswith('#')

def test_resource_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    assert response.status_code == 404