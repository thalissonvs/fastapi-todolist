from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World!'}  # Assert
