onload = function(){
    document.getElementById("difficultyField").addEventListener("input", hideError);
}

//returns if game difficulty is selected
function validateForm(){
    var diffElement = document.getElementById("difficultyField");
    var selectedDiff = diffElement.value;

    if (selectedDiff == ""){
        showError(diffElement);
        return false;
    }
    return true;
}

//resets event target style and hide associated error message
function hideError(event){
    event.target.style.outline = "none";
    document.getElementById("difficultyErrorMessage").style.visibility = "hidden";
}

//change element style and show associated error message
function showError(element){
    element.style.outline = "3px solid rgb(135, 2, 2)";
    document.getElementById("difficultyErrorMessage").style.visibility = "visible";
}