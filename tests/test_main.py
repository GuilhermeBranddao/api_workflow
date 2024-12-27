import pytest 

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200

def test_home_message():
    response = client.get("/")

    assert response.json() == {"message":"Tudo certo"}


def test_list_products():
    response = client.get("/produtos")

    assert response.status_code == 200

def test_list_find_products():
    response = client.get("/produtos/1")

    assert response.status_code == 200