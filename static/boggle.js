class BoggleGame {
    constructor(boardID) {
        this.board = $("#" + "board");
        $(".guesses", this.board).on("submit", this.handleSubmit.bind(this));

    }
}