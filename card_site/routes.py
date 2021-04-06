from flask import render_template, redirect, url_for
from flask_discord import DiscordOAuth2Session
from main import app

discord = DiscordOAuth2Session(app)


@app.route("/")
def index():
    if not discord.authorized:
        return render_template("home.html", user="e")

    user = discord.fetch_user()

    return render_template("home.html", user=user.avatar_url, username=user.name, user_id=user.id)


@app.route("/login/")
def login():
    return discord.create_session()


@app.route("/callback/")
def callback():
    data = discord.callback()
    redirect_to = data.get("redirect", "/")
    return redirect(redirect_to)


@app.route("/logout/")
def logout():
    discord.revoke()
    return redirect(url_for(".index"))

