from tests.unit_tests.conftest import client_2


def test_href_in_table_redirect_index(client_2):
    """
    Args:
        client_2 ([type]): fixture
    """
    response = client_2.get('/table')
    data = response.get_data(as_text=True)
    methode = '<a href="/">'
    assert methode in data
