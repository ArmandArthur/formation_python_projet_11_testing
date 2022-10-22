from ...server import loadCompetitions, loadClubs
from ..conftest import fixture_clubs, fixture_competitions, fixture_club_points_by_competitions, app, client, captured_templates
import pytest
from ... import server
import flask
from flask import session

def test_purchase_reponse_200(fixture_clubs, fixture_competitions, mocker, client): 
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 5
    reponse = client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    assert reponse.status_code == 200

def test_flash_message_if_not_enought_points_by_club(fixture_clubs, fixture_competitions,fixture_club_points_by_competitions, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)

    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 50
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    flash_message = 'Not enought points'
    assert flash_message in list(flask.get_flashed_messages())

def test_flash_message_if_enought_points_by_club(fixture_clubs, fixture_competitions,fixture_club_points_by_competitions, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    mocker.patch.object(server, "club_points_by_competitons", fixture_club_points_by_competitions)

    club = 'Simply Lift'
    competiton = 'Spring Festival'
    purchase_places = 5
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competiton})
    
    flash_message = 'Great-booking complete!'
    assert flash_message in list(flask.get_flashed_messages())

def test_verify_context_and_template(fixture_clubs, fixture_competitions, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    mocker.patch.object(server, "competitions", fixture_competitions)
    club = 'Simply Lift'
    competition = 'Spring Festival'
    purchase_places = 5
    client.post("/purchasePlaces", data={'places': purchase_places, 'club': club, 'competition': competition})
    template, context = captured_templates[0]
    
    # Nom du template
    assert template.name == 'welcome.html'

    # Vérifie si le club renvoit par le template est le bon...
    assert club in context['club']['name']

    competition_context = next((c for c in  context['competitions'] if c['name'] == competition), None)
    # Vérifie si la compétition est bien la liste des compétitions
    assert competition == competition_context['name']


