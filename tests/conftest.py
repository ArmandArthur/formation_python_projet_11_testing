from unittest import mock
import pytest
from .. import server
from flask import template_rendered
from contextlib import contextmanager
import pytest

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture()
def app():
    app = server.app
    app.config.update(({'TESTING': True}))
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def fixture_emails():
    return {
                "email_good" : 
                {
                    "email" : "john@simplylift.co"
                },
                "email_not_good" : 
                {
                    "email" : "john@simplylift"
                }
            }
            
@pytest.fixture
def fixture_clubs():
    return [
            {
                "name":"Simply Lift",
                "email":"john@simplylift.co",
                "points":"1500"
            },
            {
                "name":"Iron Temple",
                "email": "admin@irontemple.com",
                "points":"0"
            },
            {   "name":"She Lifts",
                "email": "kate@shelifts.co.uk",
                "points":"30"
            }
        ]


@pytest.fixture
def fixture_competitions():
    return [
        {
            "name": "Spring Festival",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "20"
        },
        {
            "name": "Spring Festival Past",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "20"
        }
    ]

@pytest.fixture
def fixture_club_points_by_competitions():
    return {}
   


