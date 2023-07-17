import pytest

from flask import g, session
from api.v1.db import get_db


def test_register(client, app):
    assert client.get("/api/v1/auth/register").status_code == 200
    response = client.post(
        "/auth/register", data={"username": "a", "password_hash": "a"}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert (
            get_db().execute("select * from users where username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password_hash", "message"),
    (
        ("", "", "Username is required."),
        ("a", "", "Password is required."),
        ("test", "test", "already registered"),
    ),
)
def test_register_validate_input(client, username, password_hash, message):
    response = client.post(
        "/api/v1/auth/register",
        json={"username": username, "password_hash": password_hash},
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password_hash", "message"),
    (
        ("a", "test", "Incorrect username."),
        ("test", "a", "Incorrect password."),
    ),
)
def test_login_validate_input(auth, username, password_hash, message):
    response = auth.login(username, password_hash)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
