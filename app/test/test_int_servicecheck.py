"""API test cases for service check API"""
from falcon import testing, falcon
import pytest

from app.server import create_server


@pytest.fixture()
def client():
    return testing.TestClient(create_server())

def test_int_servicecheck(client):
    res = client.simulate_get("/servicecheck")
    assert res.status == falcon.HTTP_200
