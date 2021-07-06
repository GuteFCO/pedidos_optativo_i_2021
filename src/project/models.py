import uuid
from . import db


class Pedido(db.Model):
    def __init__(self, *args, **kwargs):
        super(Pedido, self).__init__(*args, **kwargs)
        self.uuid = str(uuid.uuid4())

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    uuid = db.Column(db.String, nullable=True)
