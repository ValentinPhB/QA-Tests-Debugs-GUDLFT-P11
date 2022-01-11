from tests.unit_tests.conftest import client


def test_points_and_places_should_not_change_book_more(client):
    """
    Test: logged club wants to book more places than number available.
    Number of places for a tournament should not change.
    Points available of the club should not change.
    Message : 'You can not book {places} places for this competition. Only {number_place_available} places left.'
     has to be displayed.

    Args:
        client ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    places = 6

    comp_name = 'Small'
    comp_places = 3

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'You can not book {places} places for this competition. Only {comp_places} places left.'

    message_expected_club_points_unchanged = f"Points available: {club_points_available}"

    message_expected_places_comp_unchanged = f"Number of Places: {comp_places}"

    data = response.get_data(as_text=True)

    # Check if data needed is ok.
    assert response.status_code == 200
    # Check if "conditional if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Check if points_available is unchanged.
    assert message_expected_club_points_unchanged in data
    # Check if places_competition is unchanged.
    assert message_expected_places_comp_unchanged in data
