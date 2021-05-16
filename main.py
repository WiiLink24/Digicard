import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.secret_key = config.secret_key
if app.debug:
    # !! Only use in a development environment.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"

app.config["DISCORD_CLIENT_ID"] = config.discord_client_id
app.config["DISCORD_CLIENT_SECRET"] = config.discord_client_secret
app.config["DISCORD_REDIRECT_URI"] = config.discord_redirect_uri
if __name__ == "__main__":
    app.run()

import card_site
