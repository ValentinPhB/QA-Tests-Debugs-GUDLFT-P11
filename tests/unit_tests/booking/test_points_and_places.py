from app import loadClubs, loadCompetitions
import random


def test_points_and_places_should_not_change(client):
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

    club_name = club['name']
    club_points_available = int(club['points'])

    # More places asks than points available.
    places = (club_points_available + 1)

    comp_name = "Spring Festival"
    comp_places = 25

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = 'Your club do not have enough points to do this.'

    wrong_count_points = club_points_available - places
    message_expected_club_points_updated = f"Points available: {wrong_count_points}"

    wrong_count_places = comp_places - places
    message_expected_places_comp_updated = f"Number of Places: {wrong_count_places}"

    data = response.get_data(as_text=True)

    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Cheking if points_avalable is unchanged.
    assert message_expected_club_points_updated not in data
    # Cheking if places_competition is unchanged.
    assert message_expected_places_comp_updated not in data


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

    comp_name = "Fall Classic"
    comp_places = 13

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = 'Great-booking complete!'

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
