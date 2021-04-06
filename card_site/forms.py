from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import (
    SubmitField,
    FileField,
)


class UploadCard(FlaskForm):
    card = FileField("Business Card")
    upload = SubmitField("Upload Card")
