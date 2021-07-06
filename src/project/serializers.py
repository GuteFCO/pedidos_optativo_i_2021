from . import ma
from .models import Pedido


class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedido
        load_instance = True
        read_only = ('uuid',)
