from tests.unit_tests.conftest import client


def test_display_table_contains_all_clubs_and_their_points(client):
    """
    Test: Unlogged club (on table.html) can see a table with all clubs and their points.
    Number of points displayed has to be correct and correctly affiliate to his club.

    Args:
        client ([type]): Fixture
    """
    response = client.get('/table')
    data = response.get_data(as_text=True)

    # To facilitate tests, points have a special html class as follow :
    club_1 = "Simply Lift"
    points_club_1 = f'<td class="{club_1}">13</td>'
    
    club_2 = "Iron Temple"
    points_club_2 = f'<td class="{club_2}">4</td>'
    
    club_3 = "She Lifts"
    points_club_3 = f'<td class="{club_3}">12</td>'
    
    assert response.status_code == 200
    # Check if club_1 is well named and affiliate to his points :
    assert club_1 and points_club_1 in data
    # Check if club_2 is well named and affiliate to his points :
    assert club_2 and points_club_2 in data
    # Check if club_3 is well named and affiliate to his points :
    assert club_3 and points_club_3 in data
