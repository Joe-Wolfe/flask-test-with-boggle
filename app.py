from flask import Flask, render_template, request, session
from boggle import Boggle


app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

boggle_game = Boggle()


@app.route("/")
def home():
    """The page with the boggle board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)
    return render_template("index.html", board=board, highscore=highscore, numplays=numplays)
