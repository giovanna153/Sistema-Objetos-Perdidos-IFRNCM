from app.models.objeto import Objeto


def listar_objetos():
    return Objeto.query.order_by(Objeto.id.desc()).all()