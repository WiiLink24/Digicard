from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    FileField,
    StringField
)
from wtforms.validators import InputRequired


class UploadCard(FlaskForm):
    card = FileField("Business Card", validators=[InputRequired()])
    card_id = StringField("Order ID", validators=[InputRequired()])
    upload = SubmitField("Upload Card")
