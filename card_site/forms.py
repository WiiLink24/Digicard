from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import (
    SubmitField,
    FileField,
)


class UploadCard(FlaskForm):
    card = FileField("Business Card",
                     validators=[FileRequired(),
                                 FileAllowed(['jpg', 'png'], 'Images only!')
                                 ]
                     )
    upload = SubmitField("Upload Card")
