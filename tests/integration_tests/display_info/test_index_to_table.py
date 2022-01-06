from tests.unit_tests.conftest import client_2


def test_href_in_index_redirect_table(client_2):
    """
    Args:
        client_2 ([type]): fixture
    """
    response = client_2.get('/')
    data = response.get_data(as_text=True)
    methode = '<a href="/table">'
    assert methode in data
    