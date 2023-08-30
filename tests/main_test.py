import pytest
from fastapi.testclient import TestClient
from main import app


def test_case()


client = TestClient(app)

# Testing adding of an item
response = client.post('/items/', json={'name': 'New Item', 'price': 50})
assert response.status_code == 200
assert response.json() == {'name': 'New Item', 'price': 50}

# Testing updating of an item
response = client.put(
    '/items/1', json={'name': 'Updated Item', 'price': 100})
assert response.status_code == 200
assert response.json() == {'name': 'Updated Item', 'price': 100}
