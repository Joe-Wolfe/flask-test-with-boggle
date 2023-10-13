from flask import Flask, render_template, request, session, jsonify
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


@app.route("/check")
def check():
    """Checks the given word to make sure it is valid
    Avalid word must
    1. Be a valid word found in words.txt
    2. Be a valid move on the boggle board.  

    returns json dictionaries {“result”: “ok”} , {“result”: “not-on-board”}, or {“result”: “not-a-word”} 

    """

    guess = request.args["word"]
    board = session["board"]

    print(guess)
    response = boggle_game.check_valid_word(board, guess)

    return jsonify({"result": response})
