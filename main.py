import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"    # !! Only in development environment.

app.config["DISCORD_CLIENT_ID"] = os.getenv("SECRET_ID")
app.config["DISCORD_CLIENT_SECRET"] = os.getenv("SECRET_KEY")
app.config["DISCORD_REDIRECT_URI"] = "http://card.wiilink24.com/callback"

if __name__ == "__main__":
    app.run()

import card_site
