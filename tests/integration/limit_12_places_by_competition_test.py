from ...server import loadCompetitions, loadClubs
from ..conftest import fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, app, client, captured_templates
import pytest
from ... import server
import flask

def test_integration_flash_message_if_club_places_by_competition_is_more_than_12(fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    # 1er mock avec valeur retournée
    fixture_club_points_by_competitions = mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 5
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    flash_message = 'Great-booking complete!'
    assert flash_message in list(flask.get_flashed_messages())

    # 2ème mock avec la valeur retournée du 1er mock
    fixture_club_points_by_competitions = mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    # 3ème mock avec la valeur retournée du 2ème mock
    mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    flash_message = 'Max points is 12 for a club in a competition'
    assert flash_message in list(flask.get_flashed_messages())


