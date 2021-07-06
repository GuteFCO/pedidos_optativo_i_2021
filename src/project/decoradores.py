import requests
from functools import wraps
from flask import request
from werkzeug.exceptions import Forbidden, InternalServerError, Unauthorized


class Usuario:
    def __init__(self, id, nombre, email, direccion, edad):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.edad = edad


def autorizar(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        authorization = request.headers.get('authorization')
        response = requests.get(
            url='http://usuarios:5000/usuario_actual',
            headers={
                'Authorization': authorization
            })
        if response.ok:
            usuario = Usuario(**response.json())
            return f(usuario, *args, **kwargs)
        elif response.status_code == 401:
            raise Unauthorized
        elif response.status_code == 403:
            raise Forbidden
        else:
            raise InternalServerError
    return wrapper
