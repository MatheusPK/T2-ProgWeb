onload= function(){
    difficultySelectionChanged()
    document.getElementById("backButton").addEventListener("click", function (){
        window.history.back();
        console.log("oi")
    })
}

function difficultySelectionChanged() {
    var newValue = document.getElementById("leaderboardDifficulty").value

    switch (newValue) {
        case "easy":
            toggle("easyScore", "table-row")
            toggle("normalScore", "none")
            toggle("hardScore", "none")
            break;
        case "normal":
            toggle("easyScore", "none")
            toggle("normalScore", "table-row")
            toggle("hardScore", "none")
            break
        case "hard":
            toggle("easyScore", "none")
            toggle("normalScore", "none")
            toggle("hardScore", "table-row")
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