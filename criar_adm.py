
from app import app, db
from app.models.usuario import Usuario


def criar_admin():
    with app.app_context():
        if Usuario.query.first():
            print("Já existe um usuário cadastrado.")
            return

        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip().lower()
        senha = input("Senha: ")
        confirmar_senha = input("Confirme a senha: ")

        if not nome or not email or not senha:
            print("Todos os campos são obrigatórios.")
            return

        if senha != confirmar_senha:
            print("As senhas não coincidem.")
            return

        if Usuario.query.filter_by(nome=nome).first():
            print("Esse nome já está cadastrado.")
            return

        if Usuario.query.filter_by(email=email).first():
            print("Esse e-mail já está cadastrado.")
            return

        usuario = Usuario(
            nome=nome,
            email=email
        )

        usuario.set_senha(senha)

        try:
            db.session.add(usuario)
            db.session.commit()
            print("Primeiro usuário criado com sucesso!")
        except Exception as erro:
            db.session.rollback()
            print("Erro ao criar usuário:", erro)


if __name__ == "__main__":
    criar_admin()
