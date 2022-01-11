
from tests.unit_tests.conftest import client


def test_not_allowed_more_than_12_places_in_one_competition_at_once(client):
    """
    Test: logged club want to reserve more than 12 places at once.
    Number of places for a tournament should not change.
    Points available of the club should not change.
    Message : 'You can not book more than (12) places per competition and less than (1) if you choose to participate.'
     has to be displayed.

    Args:
        client ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    # Place = club_points_available
    places = club_points_available

    comp_name = "Future"
    comp_places = 20

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = 'You can not book more than (12) places per competition and less than (1) if you choose to participate.'

    message_expected_club_points_updated = "Points available: 0"

    count = str(comp_places - places)
    message_expected_places_comp_updated = f"Number of Places: {count}"

    data = response.get_data(as_text=True)

    # Check if data needed is ok.
    assert response.status_code == 200
    # Check if "conditional if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Check if points_available is unchanged.
    assert message_expected_club_points_updated not in data
    # Check if places_competition is unchanged.
    assert message_expected_places_comp_updated not in data

