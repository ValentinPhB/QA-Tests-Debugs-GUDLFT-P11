from tests.unit_tests.conftest import client


def test_should_return_message_empty_email(client):
    email = ""
    message_expected = "Sorry, that email was not found."
    response = client.post('/showSummary', data={'email': email})
    data = response.get_data(as_text=True)
    assert message_expected in data
    assert response.status_code == 405
