import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_contacts_unauthorized():
    response = client.get("/contacts/")
    assert response.status_code in (401, 403)
