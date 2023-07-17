from api.v1 import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/api/v1/hello")
    assert response.data == '{"message":"Hello, World!"}\n'
