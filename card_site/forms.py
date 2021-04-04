from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    FileField,
    SelectField,
    TextAreaField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, ValidationError

class UploadCard(FlaskForm):
