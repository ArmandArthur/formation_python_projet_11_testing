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
            return client

    @pytest.fixture
    def test_data_fixture(self):
        """test_data_fixture

        Returns:
            dict about dict
        """
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
