from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField(
        'E-mail',
        validators=[
            DataRequired(message='Por favor, preencha o e-mail.'),
            Email(message='E-mail inválido.')
        ]
    )

    senha = PasswordField(
        'Senha',
        validators=[
            DataRequired(message='Por favor, preencha a senha.'),
            Length(
                min=5,
                message='A senha deve ter pelo menos 5 caracteres.'
            )
        ]
    )



    submit = SubmitField("Entrar")