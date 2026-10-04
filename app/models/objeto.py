from app import db

class Objeto(db.Model):
    __tablename__ = "objeto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)
    local = db.Column(db.String(100), nullable=False)

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id'),
        nullable=False
    ) # Um Usuario pode ter vários Objeto associados a ele.
    # 1 Usuario ──────── N Objetos
    
    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey('categoria.id'),
        nullable=False
    )

    autor = db.relationship(
        'Usuario',
        back_populates='objetos'
    )

    categoria = db.relationship(
        'Categoria',
        back_populates='objetos'
    )

    devolucao = db.relationship(
        'Devolucao',
        back_populates='objeto',
        uselist=False
    )

    def __repr__(self):
        return f'<Objeto {self.nome}>'