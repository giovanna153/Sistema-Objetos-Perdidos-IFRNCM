from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class DevolucaoForm(FlaskForm):

    objeto_id = SelectField(
        'Selecione o objeto',
        coerce=int,
        validators=[
            DataRequired(message='Selecione um objeto.')
        ]
    )

    nome_aluno = StringField(
        'Nome do aluno',
        validators=[
            DataRequired(message='Informe o nome do aluno.'),
            Length(max=100)
        ]
    )

    matricula_aluno = StringField(
        'Matrícula',
        validators=[
            DataRequired(message='Informe a matrícula.'),
            Length(max=20)
        ]
    )

    turma_aluno = StringField(
        'Turma',
        validators=[
            DataRequired(message='Informe a turma.'),
            Length(max=50)
        ]
    )

    observacao = TextAreaField(
        'Observação',
        validators=[
            Length(max=500)
        ]
    )

    submit = SubmitField('Registrar devolução')