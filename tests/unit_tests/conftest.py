import pytest

from app import create_app


@pytest.fixture
def client(mocker):
    """
    Client with ratio controled by app.py.
    """
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
            "numberOfPlaces": "20"
        },
    ])
    mocker.patch('app.ratio', return_value=1)
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_2(mocker):
    """
    Client for url tests and get better coverage by test original data.
    """
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_3(mocker):
    """
    Client with determinated ratio() to control assertion.
    """
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
            "numberOfPlaces": "20"
        },
    ])
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client
