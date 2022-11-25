function difficultySelectionChanged() {
    var newValue = document.getElementById("leaderboardDifficulty").value
    var easyScores = document.getElementsByClassName("easyScore")
    var normalScores = document.getElementsByClassName("normalScore")
    var hardScores = document.getElementsByClassName("hardScore")
    switch (newValue) {
        case "easy":
            toggle("easyScore", "block")
            toggle("normalScore", "none")
            toggle("hardScore", "none")
            break;
        case "normal":
            toggle("easyScore", "none")
            toggle("normalScore", "block")
            toggle("hardScore", "none")
            break
        case "hard":
            toggle("easyScore", "none")
            toggle("normalScore", "none")
            toggle("hardScore", "block")
        default:
            break;
    }
}

function toggle(className, displayState){
    var elements = document.getElementsByClassName(className)

    for (var i = 0; i < elements.length; i++){
        elements[i].style.display = displayState;
    }
}