from app import db


class Cadastro(db.Model):
    __tablename__ = 'cadastros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    objetos = db.relationship(
        'Objeto',
        back_populates='cadastro'
    )