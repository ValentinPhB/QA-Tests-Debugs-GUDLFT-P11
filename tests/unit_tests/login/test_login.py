from flask import request
from tests.unit_tests.conftest import client


def test_should_status_code_200_for_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_should_return_status_200_good_email(client):
    email = "admin@irontemple.com"
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

def test_should_return_status_405_wrong_email(client):
    email = "wrong@gmail.com"
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 405

def test_should_return_status_405_empty_email(client):
    email = ""
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 405

def test_should_return_message_bad_email(client):
    email = "wrong@gmail.com"
    message_expected = "Sorry, that email was not found."
    response = client.post('/showSummary', data={'email': email})
    data = response.get_data(as_text=True)
    assert message_expected in data
    
def test_should_return_message_empty_email(client):
    email = ""
    message_expected = "Sorry, that email was not found."
    response = client.post('/showSummary', data={'email': email})
    data = response.get_data(as_text=True)
    assert message_expected in data
