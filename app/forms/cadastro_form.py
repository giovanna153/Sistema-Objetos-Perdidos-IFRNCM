from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired, Email, Length

class CadastroForm(FlaskForm):

    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Por favor, preencha o nome.')
        ]
    )

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


    submit = SubmitField("Cadastrar")