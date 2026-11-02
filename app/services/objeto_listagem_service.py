from datetime import date, timedelta

from app.models.objeto import Objeto
from app.models.devolucao import Devolucao


def listar_objetos(dias=None, categoria=None, local=None):

    # Buscar somente objetos que ainda não foram devolvidos
    consulta = Objeto.query.outerjoin(Devolucao).filter(
        Devolucao.id.is_(None)
    )

    # Filtro por período
    if dias is not None:
        hoje = date.today()
        data_limite = hoje - timedelta(days=dias)

        consulta = consulta.filter(
            Objeto.data >= data_limite,
            Objeto.data <= hoje
        )

    # Filtro por categoria
    if categoria and categoria != "todos":
        consulta = consulta.join(Objeto.categoria).filter(
            Objeto.categoria.has(nome=categoria)
        )

    # Filtro por local
    if local and local != "todos":
        consulta = consulta.join(Objeto.local).filter(
            Objeto.local.has(nome=local)
        )

    # Ordenar do mais recente para o mais antigo
    return consulta.order_by(Objeto.id.desc()).all()