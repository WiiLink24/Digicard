from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    FileField,
)


class UploadCard(FlaskForm):
    card = FileField("Business Card")
    upload = SubmitField("Upload Card")
