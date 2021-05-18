from main import app
from flask import send_from_directory


@app.route("/cards/<discord_id>.jpg")
def digicard(discord_id):
    return send_from_directory("./cards", discord_id  + ".jpg")

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


