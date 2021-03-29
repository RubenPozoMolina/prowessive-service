import requests
import constants
import pytest


@pytest.fixture
def project():
    body = {
        "data": "test",
        "name": "test"
    }
    response = requests.post(constants.host + '/projects/',
                             headers=constants.header,
                             json=body
                             )
    yield response.json()
    requests.delete(constants.host + '/projects/test',
                    headers=constants.header
                    )


class TestProjects:

    def test_get_project(self, project):
        response = requests.get(constants.host + '/projects/' + str(project['name']),
                                headers=constants.header)
        assert response.status_code == 200
        assert response.json() == project
