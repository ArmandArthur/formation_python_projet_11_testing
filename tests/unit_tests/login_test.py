from ...server import loadCompetitions, loadClubs
from .fixture_test import TestFixture

competitions = loadCompetitions()  
clubs = loadClubs()  


class TestLogin(TestFixture):
    def test_email_in_list(self, client, test_data_fixture):
        response = client.post("/showSummary", data={'email': test_data_fixture['email_good']['email']})
        assert response.status_code == 200

    def test_email_not_in_list(self, client, test_data_fixture):
        response = client.post("/showSummary", data={'email': test_data_fixture['email_not_good']['email']})
        assert response.status_code == 301
    

    def test_mock_points_superior_ten(self, test_mocker_club_points_fixture):
        ten_superior_club = next(club for club in test_mocker_club_points_fixture if int(club['points']) >= 10)
        assert len(ten_superior_club) == len(test_mocker_club_points_fixture)

