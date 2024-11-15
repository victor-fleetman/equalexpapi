import pytest
from app import app  # Import the Flask application instance

@pytest.fixture
def client():
    return app.test_client()

def test_root_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "<strong>Welcome to the Gist API!</strong>" in response.data.decode()

def test_username_route(client):
    response = client.get('/octocat')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert 'gists' in response.json
    assert len(response.json['gists']) > 0
