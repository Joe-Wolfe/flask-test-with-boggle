class BoggleGame {
    constructor() {
        this.board = $("#game");
        $(".guesses", this.board).on("submit", this.handleSubmit.bind(this));

    }

    async handleSubmit(evt) {
        evt.preventDefault();
        let word = $("#user-guess").val();
        console.log(word);

        $("#user-guess").val("").focus();
    }
}