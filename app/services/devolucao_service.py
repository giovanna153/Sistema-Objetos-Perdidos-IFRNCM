from app import db
from app.models.devolucao import Devolucao
from app.models.objeto import Objeto
from datetime import datetime


def cadastrar_devolucao(form):

    objeto = db.session.get(Objeto, form.objeto_id.data)

    if objeto is None:
        raise ValueError("Objeto não encontrado.")

    if objeto.devolucao is not None:
        raise ValueError("Este objeto já foi devolvido.")

    devolucao = Devolucao(
        objeto_id=objeto.id,
        nome_objeto=objeto.nome_objeto,
        nome_aluno=form.nome_aluno.data.strip(),
        matricula_aluno=form.matricula_aluno.data.strip(),
        turma_aluno=form.turma_aluno.data.strip(),
        observacao=form.observacao.data.strip() or None,
        data_devolucao=datetime.now()
    )

    db.session.add(devolucao)
    db.session.commit()

    return devolucao


def listar_devolucoes():

    return Devolucao.query.order_by(
        Devolucao.data_devolucao.desc()
    ).all()