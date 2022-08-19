import datetime
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


def create_token(id):
    payload = {
        'id': id,
        'expiration': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=60)),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'access_secret', algorithm='HS256')
    return token


def decode_token(token):
    data = jwt.decode(token, 'secret', algorithms=['HS256'])
    if data is not None:
        return data['id']
    return AuthenticationFailed('User not found!')


def refresh_token(token):
    idd = decode_token(token)
    if id is not None:
        return create_token(idd)
    return AuthenticationFailed('User not found!')
