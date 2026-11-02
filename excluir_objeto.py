from app import app, db
from app.models.objeto import Objeto
from app.models.devolucao import Devolucao


with app.app_context():

    objetos = Objeto.query.all()

    for objeto in objetos:
        print(objeto.id, objeto.nome_objeto)

    id_objeto = int(input("Digite o ID do objeto que deseja excluir: "))

    objeto = db.session.get(Objeto, id_objeto)

    if objeto:

        devolucao = Devolucao.query.filter_by(
            objeto_id=objeto.id
        ).first()

        if devolucao:
            db.session.delete(devolucao)
            
        db.session.delete(objeto)

        db.session.commit()

        print("Objeto excluído com sucesso!")

    else:
        print("Objeto não encontrado.")