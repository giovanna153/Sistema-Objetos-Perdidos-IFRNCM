from app import app, db
from app.models.objeto import Objeto


with app.app_context():
    objetos = Objeto.query.all()


    for objeto in objetos:
        print(objeto.id, objeto.nome_objeto)


    id_objeto = int(input("Digite o ID do objeto que deseja excluir: "))


    objeto = db.session.get(Objeto, id_objeto)


    if objeto:
        db.session.delete(objeto)
        db.session.commit()
        print("Objeto excluído com sucesso!")
    else:
        print("Objeto não encontrado.")
