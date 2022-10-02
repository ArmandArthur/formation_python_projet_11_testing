from ..server import loadCompetitions, loadClubs

competitions = loadCompetitions()  
clubs = loadClubs()  

def test_email_in_list(client):
    """
        test_email_in_list
    """
    response = client.post("/showSummary", data={'email': 'john@simplylift.co'})
    assert response.status_code == 200

def test_email_not_in_list(client):
    """
        test_email_not_in_list
    """
    response = client.post("/showSummary", data={'email': 'john@simplylift'})
    assert response.status_code == 301

