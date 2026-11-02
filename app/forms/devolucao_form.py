from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class DevolucaoForm(FlaskForm):

    objeto_id = SelectField(
        'Selecione o objeto',
        coerce=int,
        validators=[DataRequired(message='Selecione um objeto.')]
    )

    nome_aluno = StringField(
        'Nome do aluno',
        validators=[DataRequired()]
    )

    matricula_aluno = StringField(
        'Matrícula',
        validators=[DataRequired()]
    )

    turma_aluno = StringField(
        'Turma',
        validators=[DataRequired()]
    )

    nome_objeto = StringField(
        'Nome do objeto',
        validators=[DataRequired()]
    )

    observacao = TextAreaField(
        'Observação',
        validators=[Length(max=500)]
    )

    submit = SubmitField('Registrar devolução')