import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

@pytest.fixture
def client_2(mocker):
    mocker.patch('app.loadCompetitions', return_value=[
        {
            'name': 'Spring Festival',
            'date': '2020-03-27 10:00:00',
            'numberOfPlaces': '25'
        },
        {
            'name': 'Fall Classic',
            'date': '2020-10-22 13:30:00',
            'numberOfPlaces': '13'
        },
        {
            'name': 'Small',
            'date': '2024-09-14 15:30:00',
            'numberOfPlaces': '3'
        },
        {
            'name': 'Future',
            'date': '2026-01-22 17:00:00',
            'numberOfPlaces': '8'
        }
    ])
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client
