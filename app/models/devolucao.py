from app import db
from datetime import datetime


class Devolucao(db.Model):
    __tablename__ = 'devolucoes'

    id = db.Column(db.Integer, primary_key=True)

    data_devolucao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    observacao = db.Column(db.Text)

    objeto_id = db.Column(
        db.Integer,
        db.ForeignKey('objeto.id'),
        nullable=False,
        unique=True
    )

    objeto = db.relationship(
        'Objeto',
        back_populates='devolucao'
    )

    nome_aluno = db.Column(db.String(100), nullable=False)
    matricula_aluno = db.Column(db.String(20), nullable=False)
    turma_aluno = db.Column(db.String(10), nullable=False)
    nome_objeto = db.Column(db.String(100), nullable=False)