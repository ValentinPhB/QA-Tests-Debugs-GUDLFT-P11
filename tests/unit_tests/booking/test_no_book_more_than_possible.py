def test_points_and_places_should_not_change(client_2):
    """
    Test: logged club wants to book more places than number available.
    Number of places for a tournament should not change.
    Points available of the club should not change.
    Message : 'You can not book {places} places for this competition. Only {numbre_place_available} places left.' has to be displayed.

    Args:
        client_2 ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    places = 6

    comp_name = 'Small'
    comp_places = 3

    response = client_2.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'You can not book {places} places for this competition. Only {comp_places} places left.'

    message_expected_club_points_unchanged = f"Points available: {club_points_available}"

    message_expected_places_comp_unchanged = f"Number of Places: {comp_places}"

    data = response.get_data(as_text=True)

    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Cheking if points_avalable is unchanged.
    assert message_expected_club_points_unchanged in data
    # Cheking if places_competition is unchanged.
    assert message_expected_places_comp_unchanged in data
