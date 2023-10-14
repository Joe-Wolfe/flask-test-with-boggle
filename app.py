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
    numplays = session.get("numplays", 1)
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


@app.route("/score", methods=["POST"])
def post_score():
    """sends a post request to the servers  and checks if a new record has been set and updates times played"""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    session["numplays"] = numplays+1
    session['highscore'] = max(score, highscore)

    return jsonify(newRecord=score > highscore)
