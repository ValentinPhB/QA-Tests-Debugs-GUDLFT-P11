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
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Small",
            "date": "2023-09-13 15:30:00",
            "numberOfPlaces": "3"
        },
        {
            "name": "Future",
            "date": "2030-11-02 17:00:00",
            "numberOfPlaces": "10"
        },
    ])
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client
