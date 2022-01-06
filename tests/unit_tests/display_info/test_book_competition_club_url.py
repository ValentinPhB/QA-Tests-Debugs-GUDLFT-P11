from tests.unit_tests.conftest import client
from app import loadCompetitions


def test_display_information_book_url_if_competition_or_club_exists(client):
    club_1 = "Simply Lift"
    club_2 = "Iron Temple"
    wrong_club = "Wrong club"
    wrong_competition = "Wrong competition"

    competitions = loadCompetitions()

    for competition in competitions:
        if int(competition['numberOfPlaces']) > 0:
            response = client.get(f"/book/{competition['name']}/{club_1}")
            assert response.status_code == 200

            response_2 = client.get(f"/book/{competition['name']}/{club_2}")
            assert response_2.status_code == 200

            response_3 = client.get(
                f"/book/{competition['name']}/{wrong_club}")
            message_expected = 'Something went wrong-please try again'
            data = response_3.get_data(as_text=True)
            assert message_expected in data

            response_4  = client.get(
                f"/book/{wrong_competition}/{club_1}")
            data_2 = response_4.get_data(as_text=True)
            assert message_expected in data_2
