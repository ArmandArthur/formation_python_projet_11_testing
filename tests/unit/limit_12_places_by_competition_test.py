from ...server import loadCompetitions, loadClubs
from .fixture_test import fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, app, client, captured_templates
import pytest
from ... import server
import flask

def test_unit_flash_message_if_club_places_by_competition_is_more_than_12(fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 13
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    flash_message = 'Max points is 12 for a club in a competition'
    assert flash_message in list(flask.get_flashed_messages())




