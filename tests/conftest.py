import pytest
import os

from booker.client import BookerClient


@pytest.fixture(scope='session')
def client():
    base = os.environ.get('BOOKER_BASE_URL')
    return BookerClient(base_url=base) if base else BookerClient()


@pytest.fixture(scope='session')
def auth_token(client):
    # Default credentials documented in examples; if different, set env vars
    username = os.environ.get('BOOKER_USER', 'admin')
    password = os.environ.get('BOOKER_PASS', 'password123')
    resp = client.auth(username, password)
    assert resp.status_code == 200, f"Auth failed: {resp.status_code} {resp.text}"
    data = resp.json()
    return data.get('token')


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 123,
        "depositpaid": False,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-02"},
        "additionalneeds": "Breakfast"
    }
