from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from flask_login import login_user, login_required, logout_user

from app import app, db
from app.models.usuario import Usuario
from app.forms.cadastro_form import CadastroForm
from app.forms.login_form import LoginForm


@app.route('/')
def index():
    return render_template('index.html')

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


@app.route("/cadastro", methods=["GET", "POST"])
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

        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('cadastro.html', form=form)