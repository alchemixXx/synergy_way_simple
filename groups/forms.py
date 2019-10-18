from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewGroupForm(FlaskForm):
    name = StringField("*Name", validators=[DataRequired(), Length(2)])
    description = StringField("Description")
    submit = SubmitField('Create')


class UpdateGroupForm(FlaskForm):
    name = StringField("*Name", validators=[DataRequired(), Length(2)])
    description = StringField("Description")
    submit = SubmitField('Save')

