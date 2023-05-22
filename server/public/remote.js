// --------- handles different input types keyboard and mouse, calls integration with robot control ----------
let default_mode = "manual";
let current_mode = null;
let is_pathing = false;


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
        if (c[i].id != "s_button" && c[i].id != "m_button"){
            c[i].style.backgroundColor = "#0a5b68b4";
        }
    }

    button_direction('s');
}

// when a button is held down by mouse, colour it lighter and start movement in the corresponding direction
function buttonPressInput(buttonID, direction){
    document.getElementById(buttonID).style.backgroundColor = "rgba(6, 51, 56, 0.71)";

    if(direction=="autonomous" || direction=="manual"){
        if(direction=="autonomous"){
            document.getElementById("m_button").style.backgroundColor = "#0a5b68b4";
        } else if (direction == "manual"){
            document.getElementById("a_button").style.backgroundColor = "#0a5b68b4";
        }
        switch_control_mode(direction);
    } else if (direction=="path" && !is_pathing){
        document.getElementById("m_button").style.backgroundColor = "#0a5b68b4";
        document.getElementById("a_button").style.backgroundColor = "#0a5b68b4";
        find_path();
        is_pathing = true;
    } else if (direction=="path" && is_pathing){
        abortPathing();
        is_pathing = false;
    }
    button_direction(direction);
}

// when a button is released by mouse, colour it darker and stop movement
function buttonReleaseInput(buttonID){
    if(buttonID !== 'a_button' &&  buttonID !== 'm_button' && buttonID !== 'best_button'){
        document.getElementById(buttonID).style.backgroundColor = "#0a5b68b4";
        button_direction('s');
    }

}

function abortPathing(){
    switch_control_mode("manual");
    document.getElementById("m_button").style.backgroundColor = "rgba(6, 51, 56, 0.71)";
    document.getElementById("best_button").style.backgroundColor = "#0a5b68b4";
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
    current_mode = new_mode;
    document.getElementById("control_mode_demo").innerHTML = new_mode;

}

function get_control_mode(){
    if (current_mode) {
        document.getElementById("test_default_mode").innerHTML = current_mode;
        return current_mode;
    } else {
        document.getElementById("test_default_mode").innerHTML = default_mode;
        return default_mode;
    }
}

// execute AStar
function find_path(){
    document.getElementById("control_mode_demo").innerHTML = "started AStar pathing";

}