from tests.unit_tests.conftest import client

def test_points_and_places_should_be_updated(client):
    """
    Test: logged club use <= than their points allowed.
    Number of places for a tournament should be updated.
    Points available of the club should be updated.
    Message : 'Great-booking complete!' has to be displayed.

    Args:
        client ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    places = 10

    comp_name = "Future"
    comp_places = 20

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'Great-booking complete! You have book {places} places.'

    message_expected_club_points_updated = f"Points available: {club_points_available - places}"

    count_2 = comp_places - places
    message_expected_places_comp_updated = f"Number of Places: {count_2}"

    data = response.get_data(as_text=True)

    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Cheking if points_avalable is updated.
    assert message_expected_club_points_updated in data
    # Cheking if places_competition is updated.
    assert message_expected_places_comp_updated in data
