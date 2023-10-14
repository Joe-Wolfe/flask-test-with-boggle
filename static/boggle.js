class BoggleGame {
    constructor() {
        this.board = $("#game");
        this.score = 0;
        $(".guesses", this.board).on("submit", this.handleSubmit.bind(this));

        this.seconds = 60;
        this.timer = setInterval(this.countdown.bind(this), 1000);

    }

    async handleSubmit(evt) {
        evt.preventDefault();

        if (this.seconds === 0) return;
        let word = $("#user-guess").val();

        $("#user-guess").val("").focus();
        const response = await axios.get("/check", {
            params: {
                word: word
            }
        });
        switch (response.data.result) {
            case ("not-word"): this.showMessage(word + " is not a valid Enlish word."); break;
            case ("not-on-board"): this.showMessage(word + " is not a playable word."); break;
            default:
                this.showMessage("congrats you found '" + word) + "'!";
                this.score += word.length;
                this.updateScore();
        }
    }

    showMessage(msg) {
        $("#msg").text(msg)
    }

    updateScore() {
        console.log(this.score)
        $("#score").text(this.score);
    }

    updateTimer() {
        $("#timer").text(this.seconds);

    }

    async countdown() {
        console.log(this.seconds)
        this.seconds -= 1;
        this.updateTimer();

        if (this.seconds === 0) {
            clearInterval(this.timer);
            await this.gameOver()
        }
    }

    async gameOver() {
        $("#user-guess").prop("disabled", true).attr("placeholder", "Time is up!");
        const response = await axios.post("/score", { score: this.score });
        if (response.data.newRecord === true) {
            this.showMessage(`New record: ${this.score}`);
        } else {
            this.showMessage(`Final score: ${this.score}`);
        }
    }
}