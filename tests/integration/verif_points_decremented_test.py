from ...server import loadCompetitions, loadClubs
from ..conftest import fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, app, client, captured_templates
import pytest
from ... import server
import flask

def test_integration_points_decremented_dashboard(fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, mocker, client, captured_templates):  

    club_before_points = next((club['points'] for club in fixture_clubs if club["name"] == 'Simply Lift'), None)
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    # 1er mock avec valeur retournée
    fixture_club_points_by_competitions = mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
   
    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 5



    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    template, context = captured_templates[0]
    
    assert context['club']['name'] == club
    assert int(club_before_points) == int(context['club']['points'])+purchase_places



    # 2ème mock avec la valeur retournée du 1er mock
    fixture_club_points_by_competitions = mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    club_before_points = int(club_before_points) - purchase_places
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    assert int(club_before_points) == int(context['club']['points'])+purchase_places



    # 3ème mock avec la valeur retournée du 2ème mock
    mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)
    club_before_points = int(club_before_points) - purchase_places
    purchase_places = 2
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    assert club_before_points == int(context['club']['points'])+purchase_places


