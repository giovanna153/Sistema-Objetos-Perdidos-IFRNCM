from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model, UserMixin ):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), index= True, unique=True, nullable=False)
    email = db.Column(db.String(120), index= True, unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    objetos = db.relationship(
        'Objeto',
        back_populates='autor' # usuário (administrador/responsável) pode estar relacionado a vários objetos cadastrados por ele.
    )

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha) # scrypt:32768:8:1$Xld6X48ENyIQ... Por segurança aparece apenas a hash da senha, e não a senha em si no sqlite.

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f'<Usuario {self.nome}>'