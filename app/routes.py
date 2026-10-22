from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from app import app, db

from app.models.usuario import Usuario
from app.models.objeto import Objeto
from app.models.categoria import Categoria

from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm
from app.forms.objeto_form import ObjetoForm

from app.services.objeto_service import cadastrar_objeto
from app.services.objeto_listagem_service import listar_objetos

from app.models.local import Local

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
        try:
            cadastrar_objeto(form, usuario_id=current_user.id)

            flash("Objeto cadastrado com sucesso!", "success")
            return redirect(url_for("dashboard"))

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
    objetos = listar_objetos()
    return render_template("objetos.html", objetos=objetos)

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