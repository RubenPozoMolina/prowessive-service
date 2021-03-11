import requests


def test_user():
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    body = {
        "email": "test@localhost.com",
        "password": "S3cr3tP4ssw0rd"
    }
    response = requests.post('http://localhost:8000/users/',
                             headers=header,
                             json=body
                             )
    print(response.text)
    assert response.status_code == 200
