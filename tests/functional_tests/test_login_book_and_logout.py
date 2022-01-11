from tests.unit_tests.conftest import client


def test_login_book_places_and_logout(client):
    # login :
    email = "admin@irontemple.com"
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

    # Book places :
    club_name = "Iron Temple"
    club_points_available = 4

    places = 2

    comp_name = "Future"
    comp_places = 20

    response = client.post(
        '/purchasePlaces', data={'club': club_name, 'competition': comp_name, 'places': places})

    message_expected = f'Great-booking complete! You have book {places} places.'

    message_expected_club_points_updated = f"Points available: {club_points_available - places}"

    count_2 = comp_places - places
    message_expected_places_comp_updated = f"Number of Places: {count_2}"

    data = response.get_data(as_text=True)

    # Check if data needed is ok.
    assert response.status_code == 200
    # Check if "conditional if " in purchasePLaces redirect correctly.
    assert message_expected in data
    # Check if points_available is updated.
    assert message_expected_club_points_updated in data
    # Check if places_competition is updated.
    assert message_expected_places_comp_updated in data
    
    # Logout : 
    response_3 = client.get('/logout')
    data_2 = response_3.get_data(as_text=True)
    methode = '<p>You should be redirected automatically to target URL: <a href="/">'
    assert methode in data_2
