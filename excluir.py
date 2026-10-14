from app import app, db
from app.models.usuario import Usuario


with app.app_context():
    usuarios = Usuario.query.all()


    for usuario in usuarios:
        print(usuario.id, usuario.nome, usuario.email)


    id_usuario = int(input("Digite o ID do usuário que deseja excluir: "))


    usuario = db.session.get(Usuario, id_usuario)


    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")
