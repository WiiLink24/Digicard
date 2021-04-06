from main import app
from card_site.forms import UploadCard
from card_site.helpers import save_card_data
from flask import render_template, redirect, flash
from werkzeug.exceptions import Forbidden
from flask_discord import DiscordOAuth2Session

discord = DiscordOAuth2Session(app)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if not discord.authorized:
        return Forbidden

    user = discord.fetch_user()
    form = UploadCard()

    if form.validate_on_submit():
        card = form.card.data

        if card:
            card_data = card.read()

            save_card_data(discord.user_id, card_data)

            return redirect("/view")
        else:
            flash("Only Digicam Business Cards are allowed")

    return render_template("upload_card.html", form=form, user=user.avatar_url, username=user.name, user_id=user.id)
