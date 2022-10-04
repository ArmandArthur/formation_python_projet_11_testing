from unittest import mock
import pytest
from ...server import app


class TestFixture:
    @pytest.fixture
    def app(self):
        tested_app = app
        with tested_app.app_context():
            yield tested_app

    @pytest.fixture
    def client(self, app):
        with app.test_client() as client:
            yield client

    @pytest.fixture
    def test_data_fixture(self):
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
    def test_mocker_club_points_fixture(self):
        return [
                {
                    "name":"Simply Lift",
                    "email":"john@simplylift.co",
                    "points":"100"
                },
                {
                    "name":"Iron Temple",
                    "email": "admin@irontemple.com",
                    "points":"50"
                },
                {   "name":"She Lifts",
                    "email": "kate@shelifts.co.uk",
                    "points":"110"
                }
            ]
