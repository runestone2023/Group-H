// --------- handles different input types keyboard and mouse, calls integration with robot control ----------

// handles retrieving input from the slider and reflecting it back to the view
function sliderUpdate(){
    let new_speed = document.getElementById("myRange").value;
    document.getElementById("speed").innerHTML = new_speed;
    speed_slider(new_speed);
}

// Handles keyboard input. Calls corresponding button_direction function.
// Colours buttons like clicking would.
function keyPressInput(event) {
    event.preventDefault();
    let key = event.key;

    // allow steering via arrow keys or WASD
    if (key == "ArrowDown" || key == "s" || key == "S") {
        document.getElementById("b_button").style.backgroundColor = "rgba(6, 51, 56, 0.71)";
        button_direction('b');
    } else if (key == "ArrowUp" || key == "w" || key == "W") {
        document.getElementById("f_button").style.backgroundColor = "rgba(6, 51, 56, 0.71)";
        button_direction('f');
    } else if (key == "ArrowLeft" || key == "a"|| key == "A") {
        document.getElementById("l_button").style.backgroundColor = "rgba(6, 51, 56, 0.71)";
        button_direction('l');
    } else if (key == "ArrowRight" || key == "d"|| key == "D") {
        document.getElementById("r_button").style.backgroundColor = "rgba(6, 51, 56, 0.71)";
        button_direction('r');
    }
}

// Recolours the buttons when they are no longer pressed by keyboard
function keyReleaseRecolour(event){
    let c = document.getElementsByClassName("button");
    for (let i=0; i<c.length; i++) {
        if (c[i].id != "s_button"){
            c[i].style.backgroundColor = "#0a5b68b4";
        }
    }

    button_direction('s');
}

// when a button is held down by mouse, colour it lighter and start movement in the corresponding direction
function buttonPressInput(buttonID, direction){
    document.getElementById(buttonID).style.backgroundColor = "rgba(6, 51, 56, 0.71)";
    if(direction=="autonomous" || direction=="manual"){
        switch_control_mode(direction);
    } else if (direction=="path"){
        find_path();
    }
    button_direction(direction);
}

// when a button is released by mouse, colour it darker and stop movement
function buttonReleaseInput(buttonID){
    document.getElementById(buttonID).style.backgroundColor = "#0a5b68b4";
    button_direction('s');
}


// --------------------------------------- Add integrations into functions below ----------------------------------------------------

// Passes the direction chosen by the buttons
function button_direction(direction){
    let text = "direction: ";
    document.getElementById("direct_demo").innerHTML = text + direction;
}

// Passes the speed chosen by the slider
function speed_slider(new_speed){
    let text = "speed: ";
    document.getElementById("speed_demo").innerHTML = text + new_speed;
}

// toggle manual / autonomous control (default should be control)
function switch_control_mode(new_mode){
    document.getElementById("control_mode_demo").innerHTML = new_mode;
}

// execute AStar
function find_path(){
    document.getElementById("control_mode_demo").innerHTML = "started AStar pathing";

}
