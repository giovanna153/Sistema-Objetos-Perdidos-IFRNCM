
from app import db
from app.models.objeto import Objeto


def cadastrar_objeto(form, usuario_id):
    objeto = Objeto(
        nome_objeto=form.nome.data,
        descricao=form.descricao.data,
        tipo=form.tipo.data,
        data=form.data.data,
        local=form.local.data,
        categoria_id=form.categoria_id.data,
        usuario_id=usuario_id,
        nome_encontrou=form.nome_encontrou.data,
        matricula=form.matricula.data,
        turma=form.turma.data,
    )

    db.session.add(objeto)
    db.session.commit()

    return objeto
