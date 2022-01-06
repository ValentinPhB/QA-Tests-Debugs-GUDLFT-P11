
def test_not_allowed_more_than_12_places_in_one_competition_at_once(client_2):
    """
    Test: logged club want to reserve more than 12 places at once.
    Number of places for a tournament should not change.
    Points available of the club should not shange.
    Message : 'You can not book more than (12) places per competition and less than (1) if you choose to participate.' has to be displayed.

    Args:
        client_2 ([type]): Fixture
    """
    club_name = "Simply Lift"
    club_points_available = 13

    # Place = club_points_available
    places = club_points_available

    comp_name = "Future"
    comp_places = 20

    response = client_2.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = 'You can not book more than (12) places per competition and less than (1) if you choose to participate.'

    message_expected_club_points_updated = "Points available: 0"

    count = str(comp_places - places)
    message_expected_places_comp_updated = f"Number of Places: {count}"

    data = response.get_data(as_text=True)

    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Cheking if points_avalable is unchanged.
    assert message_expected_club_points_updated not in data
    # Cheking if places_competition is unchanged.
    assert message_expected_places_comp_updated not in data

    def test_not_allowed_more_than_12_places_in_one_competition_several_times(client_2):
        """
    Test: logged club want to reserve more than 12 places at several times.
    Number of places for a tournament should be updated while total books for one competition by one club > 12.
    Points available of the club should be updated while total books for one competition by one club > 12.
    Message : 'You can not book more than (12) places per competition and less than (1) if you choose to participate.' has to be displayed when
    club wants to book more than 12 places for one competiton.
    
    Method : Using sessions(dict) who keep track of witch club has already booked places, count it and allow are not the possibility to book more.
    
    Args:
        client_2 ([type]): Fixture
    """

    club_name = "Simply Lift"
    club_points = 13

    places = 6
    places_2 = 7

    comp_name = "Future"
    comp_places = 20
    
    message_expected_club_points_updated = f"Points available: {club_points - places}"
    
    count = str(comp_places - places)
    message_expected_places_comp_updated = f"Number of Places: {count}"

    # First try (Less than 12 for one competiton/club)
    response = client_2.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})
    data = response.get_data(as_text=True)

    # Total for this club less than 12 it's ok.
    first_message_expected = f'Great-booking complete! You have book {places}.'
    
    # Cheking if data needed is ok.
    assert response.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert first_message_expected in data
    # Cheking if points_avalable is updated.
    assert message_expected_club_points_updated in data
    # Cheking if places_competition is updated.
    assert message_expected_places_comp_updated in data
    
    # Seconde try (More than 12 for one competiton/club)
    response_2 = client_2.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places_2})
    data_2 = response_2.get_data(as_text=True)
    
    # Total for this club more than 12 it's not allowed
    second_message_expected = 'You can not book more than (12) places per competition and less than (1) if you choose to participate.'

    message_expected_club_points_unchanged = f"Points available: {club_points - places}"
    
    message_expected_places_comp_unchanged = f"Number of Places: {count}"
    
    # Cheking if data needed is ok.
    assert response_2.status_code == 200
    # Cheking if "conditionnal if " in purchasePLaces redirect correctly.
    assert second_message_expected in data_2
    # Cheking if points_avalable is unchanged.
    assert message_expected_club_points_unchanged in data_2
    # Cheking if places_competition is unchanged.
    assert message_expected_places_comp_unchanged in data_2
    