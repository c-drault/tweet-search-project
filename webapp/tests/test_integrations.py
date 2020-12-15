import os
import pytest
import sys
sys.path.append("..")
from main.app import app
from flask import url_for


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'TEST'
    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    #assert b'Hello, World!' in rv.data