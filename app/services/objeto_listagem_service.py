from datetime import date, timedelta


from app.models.objeto import Objeto




def listar_objetos(dias=None, categoria=None, local=None):
    consulta = Objeto.query


    if dias is not None:
        hoje = date.today()
        data_limite = hoje - timedelta(days=dias)


        consulta = consulta.filter(
            Objeto.data >= data_limite,
            Objeto.data <= hoje
        )


    if categoria and categoria != "todos":
        consulta = consulta.join(Objeto.categoria).filter(
            Objeto.categoria.has(nome=categoria)
        )


    if local and local != "todos":
        consulta = consulta.join(Objeto.local).filter(
            Objeto.local.has(nome=local)
        )


    return consulta.order_by(Objeto.id.desc()).all()
