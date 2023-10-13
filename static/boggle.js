class BoggleGame {
    constructor() {
        this.board = $("#game");
        $(".guesses", this.board).on("submit", this.handleSubmit.bind(this));

    }

    async handleSubmit(evt) {
        evt.preventDefault();
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
                this.showMessage("congrats you found " + word) + "!";
        }
    }

    showMessage(msg) {
        $("#msg").text(msg)
    }
}