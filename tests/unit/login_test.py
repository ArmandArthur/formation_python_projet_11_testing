from ...server import loadCompetitions, loadClubs
from ...tests.unit.fixture_test import fixture_emails, fixture_clubs, app, client, captured_templates
import pytest
from ... import server


def test_should_response_200_if_email_good(fixture_clubs, fixture_emails, mocker, client):
    mocker.patch.object(server, "clubs", fixture_clubs)   
    response = client.post("/showSummary", data={'email': fixture_emails['email_good']['email']})
    assert response.status_code == 200


def test_should_response_301_if_email_not_good(fixture_clubs, fixture_emails, mocker, client):
    mocker.patch.object(server, "clubs", fixture_clubs)   
    response = client.post("/showSummary", data={'email': fixture_emails['email_not_good']['email']})
    assert response.status_code == 301


def test_should_have_good_arguments_if_email_good(fixture_clubs, fixture_emails, mocker, client, captured_templates):  
    mocker.patch.object(server, "clubs", fixture_clubs)   
    client.post("/showSummary", data={'email': fixture_emails['email_good']['email']})
    template, context = captured_templates[0]

    # Nom du template
    assert template.name == 'welcome.html'

    # Vérifie si le club existe
    assert "club" in context

    # Vérifie si les compétitions existent
    assert "competitions" in context

    # Vérifie si le club est dans la fixture
    assert context['club'] in fixture_clubs


