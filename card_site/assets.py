from main import app
from flask import send_from_directory


if app.debug:

    @app.route("/assets/<filename>.png")
    def icon(filename):
        return send_from_directory("assets", filename + ".png")


    @app.route("/assets/style.css")
    def css():
        return send_from_directory("templates", "style.css")

    @app.route("/js/<filename>.js")
    def js(filename):
        return send_from_directory("js", filename + ".js")


    @app.route("/card/<discord_id>.png")
    def digicard(discord_id):
        return send_from_directory("assets/cards", discord_id + ".png")
