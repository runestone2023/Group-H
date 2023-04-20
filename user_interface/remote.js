function myFunction(event) {
    event.preventDefault();
    let key = event.key;
    if (key == "ArrowDown" || key == "s" || key == "S") {
        let text = "You pressed to go down!";
        document.getElementById("demo").innerHTML = text;
        button_direction('f');
    } else if (key == "ArrowUp" || key == "w" || key == "W") {
        let text = "You pressed to go up!";
        document.getElementById("demo").innerHTML = text;
        button_direction('b');
    } else if (key == "ArrowLeft" || key == "a"|| key == "A") {
        let text = "You pressed to go left!";
        document.getElementById("demo").innerHTML = text;
        button_direction('l');
    } else if (key == "ArrowRight" || key == "d"|| key == "D") {
        let text = "You pressed to go right!";
        document.getElementById("demo").innerHTML = text;
        button_direction('r');
    } else if (key == " "){
        let text = "You pressed to stop!";
        document.getElementById("demo").innerHTML = text;
        button_direction('s');
    }

}

function button_direction(direction){
    let text = "direction: ";
    document.getElementById("demo").innerHTML = text + direction;
}
