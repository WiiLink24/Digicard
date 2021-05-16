from main import app
from card_site.forms import UploadCard
from card_site.helpers import save_card_data, validate_card
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
        card_id = form.card_id.data

        if card_id:
            if validate_card(card_id):
                save_card_data(card_id, discord.user_id)

                return redirect("/view")
            else:
                flash("Invalid Order ID")
        else:
            # The user somehow inputted nothing and it accepted it
            flash("Error Uploading Card")

    return render_template("upload_card.html", form=form, user=user.avatar_url, username=user.name, user_id=user.id)
