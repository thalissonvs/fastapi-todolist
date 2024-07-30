from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGHORITM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    result = decode(token, SECRET_KEY, algorithms=[ALGHORITM])
    assert result['sub'] == data['sub']
    assert result['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_user_not_found(client, user, token_fake_user):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': 'Bearer ' + token_fake_user},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
