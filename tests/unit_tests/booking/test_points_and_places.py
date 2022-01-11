
import random
from app import loadClubs, ratio
from tests.unit_tests.conftest import client


def test_points_and_places_should_not_change(client_3):
    """
    Test: logged club use more than their points allowed.
    Number of places for a tournament should not change.
    Points available of the club should not change.
    Message : 'Your club do not have enough points to do this.' has to be displayed.

    Args:
        client ([type]): Fixture
    """
    clubs = loadClubs()
    club = random.choice(clubs)

    points_for_places = ratio()
    
    club_name = club['name']
    club_points_available = int(club['points'])

    # More places asks than points available.
    places = (club_points_available + 1)

    comp_name = "Future"
    comp_places = 20

    response = client_3.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'Your club do not have enough points to do this. You need {points_for_places} '\
     'point(s) for ONE place.'

    wrong_count_points = club_points_available - places
    message_expected_club_points_updated = f"Points available: {wrong_count_points}"

    wrong_count_places = comp_places - places
    message_expected_places_comp_updated = f"Number of Places: {wrong_count_places}"

    data = response.get_data(as_text=True)

    # Check if data needed is ok.
    assert response.status_code == 200
    # Check if "conditional if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Check if points_available is unchanged.
    assert message_expected_club_points_updated not in data
    # Check if places_competition is unchanged.
    assert message_expected_places_comp_updated not in data
