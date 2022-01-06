from tests.unit_tests.conftest import client


def test_book_places_and_see_table_updated(client):
    """
    Test: Club book places for a competitons and see a table is corectly updated.
    Number of points displayed has to be correct and correctly affiliate to his club.

    Args:
        client ([type]): Fixture
    """
    response = client.get('/table')
    data = response.get_data(as_text=True)

    ## First check. To facilitate tests, points have a special html class as follow :
    club_name = "Simply Lift"
    club_base_points = 13
    points_club_table = f'<td class="{club_name}">{club_base_points}</td>'

    assert response.status_code == 200
    # Cheking club_1 is well named and affiliate to his points :
    assert club_name and points_club_table in data
    
    ## Second ; Book some places :
    places = 10

    comp_name = "Future"
    comp_places = 20

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'Great-booking complete! You have book {places} places.'

    message_expected_club_points_updated = f"Points available: {club_base_points - places}"

    count_2 = comp_places - places
    message_expected_places_comp_updated = f"Number of Places: {count_2}"

    data_2 = response.get_data(as_text=True)

    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if" in purchasePLaces redirect correctly.
    assert message_expected in data_2
    # Cheking if points_avalable is updated.
    assert message_expected_club_points_updated in data_2
    # Cheking if places_competition is updated.
    assert message_expected_places_comp_updated in data_2
    
    ## Third ; Check if table is updated :
    points_club_table_updated = f'<td class="{club_name}">{club_base_points - places}</td>'
    # Cheking if points is updated.
    assert points_club_table_updated in data_2
    
