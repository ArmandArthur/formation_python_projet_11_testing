from ...server import loadCompetitions, loadClubs
import pytest

competitions = loadCompetitions()  
clubs = loadClubs()  

@pytest.fixture
def test_data_fixture():
    data = {
                "email_good" : 
                {
                    "email" : "john@simplylift.co"
                },
                "email_not_good" : 
                {
                    "email" : "john@simplylift"
                }
            }
    return data

def test_email_in_list(client, test_data_fixture):
    """
        test_email_in_list
    """
    response = client.post("/showSummary", data={'email': test_data_fixture['email_good']['email']})
    assert response.status_code == 200

def test_email_not_in_list(client, test_data_fixture):
    """
        test_email_not_in_list
    """
    response = client.post("/showSummary", data={'email': test_data_fixture['email_not_good']['email']})
    assert response.status_code == 301

