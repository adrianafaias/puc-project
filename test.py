import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get('/')
    assert response.json() == {"Hello" : "World"}
    