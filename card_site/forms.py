from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    StringField
)
from wtforms.validators import InputRequired, Length


class UploadCard(FlaskForm):
    card_id = StringField("Order ID", validators=[InputRequired(), Length(max=14, message="Invalid Order ID"), ])
    upload = SubmitField("Upload Card")
