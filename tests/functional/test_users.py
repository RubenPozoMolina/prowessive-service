import requests
import constants


def test_user():
    body = {
        "email": "test@localhost.com",
        "password": "S3cr3tP4ssw0rd"
    }
    response = requests.post(constants.host + '/users/',
                             headers=constants.header,
                             json=body
                             )
    print(response.text)
    assert response.status_code == 200
