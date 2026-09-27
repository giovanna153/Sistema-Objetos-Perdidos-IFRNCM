from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.usuario import Usuario

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       email = request.form.get("email")
       senha = request.form.get("senha")

       usuario = Usuario.query.filter_by(email=email).first()
       
       if usuario and usuario.senha == senha:
           flash("Login realizado com sucesso!", "success")
           return redirect(url_for('dashboard'))
       else:
           flash("Email ou senha incorretos.", "error")
    return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

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
        
    return render_template('cadastro.html')