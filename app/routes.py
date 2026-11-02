from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user


from app import app, db


from app.models.usuario import Usuario
from app.models.objeto import Objeto
from app.models.categoria import Categoria
from app.models.devolucao import Devolucao


from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.forms.objeto_form import ObjetoForm
from app.forms.devolucao_form import DevolucaoForm


from app.services.objeto_service import cadastrar_objeto
from app.services.objeto_listagem_service import listar_objetos
from app.services.devolucao_service import cadastrar_devolucao
from app.services.devolucao_service import (
    cadastrar_devolucao,
    listar_devolucoes
)


from app.models.local import Local


import os
from werkzeug.utils import secure_filename


@app.route('/')
def index():
    objetos = listar_objetos()
    return render_template('index.html', objetos=objetos)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       email = form.email.data
       senha = form.senha.data
       usuario = Usuario.query.filter_by(email=email).first()
       
       if usuario and usuario.check_senha(senha):


           login_user(usuario)
           
           flash("Login realizado com sucesso!", "success")
           return redirect(url_for('dashboard'))
       else:
           flash("Email ou senha incorretos.", "error")


    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    try:
        logout_user()
        flash("Logout realizado com sucesso!", "success")
        return redirect(url_for("index"))
    except Exception:
        flash("Ocorreu um erro ao fazer logout. Tente novamente.", "error")
        return redirect(url_for("dashboard"))




@app.route("/dashboard")
@login_required #Só pode acessar /dashboard quem estiver autenticado.
def dashboard():
    return render_template("dashboard.html")






@app.route("/objetos/cadastrar", methods=["GET", "POST"])
@login_required
def cadastrar_novo_objeto():
    form = ObjetoForm()


    categorias = Categoria.query.order_by(Categoria.nome).all()
    form.categoria_id.choices = [
        (categoria.id, categoria.nome)
        for categoria in categorias
    ]


    locais_iniciais = [
        "Prédio principal",
        "Vivência",
        "Prédio anexo",
        "Núcleo",
        "Ginásio"
    ]


    for nome in locais_iniciais:
        local_existente = Local.query.filter_by(nome=nome).first()


        if not local_existente:
            db.session.add(Local(nome=nome))


    db.session.commit()


    locais = Local.query.order_by(Local.nome).all()
    form.local_id.choices = [
        (local.id, local.nome)
        for local in locais
    ]


    if form.validate_on_submit():
        caminho_foto = None


        try:
            arquivo = request.files.get("foto_camera")

            if not arquivo or not arquivo.filename:
                arquivo = request.files.get("foto_galeria")

            caminho_foto = None

            if arquivo and arquivo.filename:
                extensao = os.path.splitext(arquivo.filename)[1].lower()

                if extensao not in [".jpg", ".jpeg", ".png"]:
                    flash("Selecione uma imagem JPG ou PNG.", "error")
                    return render_template("cadastrar.html", form=form)

                nome_arquivo = secure_filename(arquivo.filename)
                nome_arquivo = f"{current_user.id}_{nome_arquivo}"

                pasta_uploads = os.path.join(
                    app.root_path,
                    "static",
                    "uploads"
                )
                os.makedirs(pasta_uploads, exist_ok=True)

                caminho_completo = os.path.join(
                    pasta_uploads,
                    nome_arquivo
                )

                arquivo.save(caminho_completo)

                caminho_foto = f"uploads/{nome_arquivo}"

            cadastrar_objeto(
                form,
                usuario_id=current_user.id,
                foto=caminho_foto
            )

            flash("Objeto cadastrado com sucesso!", "success")
            return redirect(url_for("dashboard"))

        except Exception as erro:
            db.session.rollback()
            print("ERRO AO CADASTRAR OBJETO:", repr(erro))
            flash("Não foi possível cadastrar o objeto.", "error")

        except Exception as erro:
            db.session.rollback()
            print("ERRO AO CADASTRAR OBJETO:", repr(erro))
            flash("Não foi possível cadastrar o objeto.", "error")


    return render_template("cadastrar.html", form=form)


@app.route("/criar-categorias")
def criar_categorias():
    categorias_iniciais = [
        "Eletrônicos",
        "Documentos",
        "Acessórios",
        "Material escolar",
        "Roupas",
        "Chaves",
        "Outros"
    ]


    for nome in categorias_iniciais:
        categoria = Categoria.query.filter_by(nome=nome).first()


        if not categoria:
            db.session.add(Categoria(nome=nome))


    db.session.commit()


    categorias = Categoria.query.all()
    return str([categoria.nome for categoria in categorias])


@app.route("/objetos", methods=["GET"])
def listar_objetos_cadastrados():
    recentes = request.args.get("recentes") == "7"
    categoria = request.args.get("categoria", "todos")
    local = request.args.get("local", "todos")


    objetos = listar_objetos(
        dias=7 if recentes else None,
        categoria=categoria,
        local=local
    )


    return render_template(
        "objetos.html",
        objetos=objetos,
        recentes=recentes,
        categoria_selecionada=categoria,
        local_selecionado=local
    )

@app.route('/devolucao', methods=['GET', 'POST'])
@login_required
def devolucao():

    form = DevolucaoForm()
    devolucao_registrada = None

    # Buscar objetos que ainda não foram devolvidos
    objetos = Objeto.query.outerjoin(Devolucao).filter(
        Devolucao.id.is_(None)
    ).all()

    form.objeto_id.choices = [
        (
            objeto.id,
            f"{objeto.nome_objeto} — "
            f"{objeto.categoria.nome} — "
            f"{objeto.local.nome} — "
            f"Encontrado em {objeto.data.strftime('%d/%m/%Y')}"
        )
        for objeto in objetos
    ]

    if form.validate_on_submit():

        try:
            devolucao_registrada = cadastrar_devolucao(form)

            flash(
                'Devolução registrada com sucesso!',
                'success'
            )

            return render_template(
                'devolucao.html',
                form=form,
                devolucao_registrada=devolucao_registrada
            )

        except Exception as erro:
            db.session.rollback()

            print(
                "ERRO AO CADASTRAR DEVOLUÇÃO:",
                repr(erro)
            )

            flash(
                'Não foi possível registrar a devolução.',
                'error'
            )

    return render_template(
        'devolucao.html',
        form=form,
        devolucao_registrada=devolucao_registrada
    )

@app.route('/admin/devolucoes')
@login_required
def historico_devolucoes():

    devolucoes = listar_devolucoes()

    return render_template(
        'objeto_devolvidos.html',
        devolucoes=devolucoes
    )

@app.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data


        # verificar se o e-mail já está cadastrado
        usuario_existente = Usuario.query.filter_by(email=email).first()


        if usuario_existente:
            flash('E-mail já cadastrado.', 'warning')
            return redirect(url_for('cadastro'))


        # Verificar se o nome já está cadastrado
        nome_existente = Usuario.query.filter_by(nome=nome).first()


        if nome_existente:
            flash('Nome já cadastrado.', 'warning')
            return redirect(url_for('cadastro'))


        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)


        try:
            db.session.add(novo_usuario)
            db.session.commit()


            flash('Cadastro realizado com sucesso', 'success')
            return redirect(url_for('cadastro'))


        except Exception:
            db.session.rollback()
            flash('Não foi possível realizar o cadastro.', 'error')
            return redirect(url_for('cadastro'))
       
    return render_template('cadastro.html', form=form)
