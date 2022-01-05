
def test_not_allowed_to_book_more_then_avalable(client_2):
    """
    Test: logged club want to reserve more than available places.
    Number of places for a tournament should not change.
    Points available of the club should not shange.
    Message : 'You can not book more than {number_available} for this tournament.' is displayed.

    Args:
        client ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    places = 6
    
    comp_name = 'Small'
    comp_places = 3

    response = client_2.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'You can not book more than {comp_places} for this tournament.'

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
