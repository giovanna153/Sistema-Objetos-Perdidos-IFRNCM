from app import db
from flask_login import UserMixin


class Usuario(db.Model, UserMixin ):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), index= True, unique=True, nullable=False)
    email = db.Column(db.String(120), index= True, unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    objetos = db.relationship(
        'Objeto',
        back_populates='autor'
    )

    def __repr__(self):
        return f'<Usuario {self.nome}>'