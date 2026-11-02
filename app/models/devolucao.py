from app import db
from datetime import datetime


class Devolucao(db.Model):
    __tablename__ = 'devolucoes'

    id = db.Column(db.Integer, primary_key=True)

    # Data e horário em que a devolução foi registrada
    data_devolucao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Identificação do objeto devolvido
    objeto_id = db.Column(
        db.Integer,
        db.ForeignKey('objeto.id'),
        nullable=False,
        unique=True
    )

    nome_objeto = db.Column(
        db.String(100),
        nullable=False
    )

    objeto = db.relationship(
        'Objeto',
        back_populates='devolucao'
    )

    # Dados do aluno que recebeu o objeto
    nome_aluno = db.Column(
        db.String(100),
        nullable=False
    )

    matricula_aluno = db.Column(
        db.String(20),
        nullable=False
    )

    turma_aluno = db.Column(
        db.String(50),
        nullable=False
    )

    # Observação sobre a devolução
    observacao = db.Column(
        db.Text,
        nullable=True
    )

    def __repr__(self):
        return f'<Devolucao {self.nome_objeto}>'