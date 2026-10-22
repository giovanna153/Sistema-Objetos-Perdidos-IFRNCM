
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Optional


class ObjetoForm(FlaskForm):
    nome = StringField(
        'Nome do objeto',
        validators=[
            DataRequired(message='Informe o nome do objeto.'),
            Length(max=50)
        ]
    )

    descricao = TextAreaField(
        'Descrição',
        validators=[
            DataRequired(message='Informe a descrição do objeto.'),
            Length(max=200)
        ]
    )

    data = DateField(
        'Data em que foi encontrado',
        format='%Y-%m-%d',
        validators=[
            DataRequired(message='Informe a data.')
        ]
    )

    local_id = SelectField(
        'Local onde foi encontrado',
        coerce=int,
        validators=[
            DataRequired(message='Selecione um local.')
        ]
    )

    detalhes_local = StringField(
        'Detalhes do local',
        validators=[
            DataRequired(message='Informe os detalhes do local.'),
            Length(max=100)
        ]
    )

    categoria_id = SelectField(
        'Categoria',
        coerce=int,
        validators=[
            DataRequired(message='Selecione uma categoria.')
        ]
    )

    nome_encontrou = StringField(
        'Nome de quem encontrou',
        validators=[
            DataRequired(message='Informe o nome de quem encontrou.'),
            Length(max=100)
        ]
    )

    matricula = StringField(
        'Matrícula',
        validators=[
            DataRequired(message='Informe a matrícula.'),
            Length(max=20)
        ]
    )

    turma = StringField(
        'Turma',
        validators=[
            DataRequired(message='Informe a turma.'),
            Length(max=50)
        ]
    )

    foto = FileField(
        'Foto do objeto',
        validators=[Optional()]
    )

    submit = SubmitField('Cadastrar objeto')
