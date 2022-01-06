from tests.unit_tests.conftest import client


def test_should_return_status_200_good_email(client):
    email = "admin@irontemple.com"
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

