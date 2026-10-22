
from app import db


class Objeto(db.Model):
    __tablename__ = "objeto"

    id = db.Column(db.Integer, primary_key=True)
    nome_objeto = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data = db.Column(db.Date, nullable=False)
    foto = db.Column(db.String(255), nullable=True)

    local_id = db.Column(
        db.Integer,
        db.ForeignKey("local.id"),
        nullable=False
    )
    detalhes_local = db.Column(db.String(100), nullable=False)

    nome_encontrou = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    turma = db.Column(db.String(50), nullable=False)

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey("categoria.id"),
        nullable=False
    )

    autor = db.relationship("Usuario", back_populates="objetos")
    categoria = db.relationship("Categoria", back_populates="objetos")
    local = db.relationship("Local", back_populates="objetos")
    devolucao = db.relationship(
        "Devolucao",
        back_populates="objeto",
        uselist=False
    )

    def __repr__(self):
        return f"<Objeto {self.nome_objeto}>"
