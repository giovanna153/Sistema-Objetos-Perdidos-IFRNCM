from app import db


class Local(db.Model):
    __tablename__ = "local"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    objetos = db.relationship(
        "Objeto",
        back_populates="local"
    )

    def __repr__(self):
        return f"<Local {self.nome}>"