from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Group


def choice_query():
    return Group.query


def get_pk(obj):
    return str(obj)


class NewUserForm(FlaskForm):
    username = StringField("*UserName", validators=[DataRequired(), Length(2)])
    group = QuerySelectField(query_factory=choice_query, allow_blank=False, get_pk=get_pk)
    submit = SubmitField('Create')


class UpdateUserForm(FlaskForm):
    username = StringField("*UserName", validators=[DataRequired(), Length(2)])
    group = QuerySelectField(query_factory=choice_query, allow_blank=False, get_pk=get_pk)
    submit = SubmitField('Save')
