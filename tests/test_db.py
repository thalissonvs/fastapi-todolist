from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='thalisson',
        password='minha_senha',
        email='thalisson@mail.com',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'thalisson'))

    assert user.username == 'thalisson'
