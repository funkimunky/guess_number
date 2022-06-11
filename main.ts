let myTimer = 6
let timerTimeout = 1
let ticks = 0
let ticks_to_wait = 30
let computer_number = 0
let guess_number = 0
let button_pressed = false
let program_options = ["start", "get_input", "check_number", "end"]
let program_state = program_options[0]
let led_blank = `
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
`
let led_smile = `
. . . . .
. # . # .
. . . . .
# . . . #
. # # # .
`
let led_higher = `
. . # . .
. # . # .
# . . . #
# . . . #
# . . . #
`
let led_lower = `
# . . . #
# . . . #
# . . . #
. # . # .
. . # . .
`
let led_congratulations = `
. . . . #
. . . . #
. . . # .
# . # . .
. # . . .
`
control.runInParallel(function on_run_in_parallel() {
    let ticks: number;
    while (true) {
        pause(100)
        ticks += 1
        if (ticks == ticks_to_wait) {
            ticks = 0
        }
        
    }
})
function progress_game(current_state: string) {
    if (current_state == "start") {
        start_game()
    } else if (current_state == "get_input") {
        get_input()
    } else if (current_state == "check_number") {
        check_number()
    } else if (current_state == "end") {
        end()
    }
    
}

function start_game() {
    let program_state = program_options[0]
    let computer_number = randint(1, 9)
    basic.clearScreen()
    basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
    let ticks = 0
    while (true) {
        if (button_pressed || ticks > 10) {
            ticks = 0
            break
        }
        
    }
    program_state = program_options[1]
    
}

function get_input() {
    basic.clearScreen()
    basic.showString("guess")
    let ticks = 0
    while (true) {
        basic.showNumber(guess_number)
        if (ticks > ticks_to_wait) {
            break
        }
        
    }
    let program_state = program_options[2]
    
}

function check_number() {
    let program_state: string;
    if (guess_number > computer_number) {
        basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        # . . . #
        `)
        pause(1000)
    }
    
    if (guess_number < computer_number) {
        basic.showLeds(`
        # . . . #
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        `)
        pause(1000)
    }
    
    if (guess_number == computer_number) {
        program_state = program_options[3]
    }
    
    
}

function end() {
    basic.showLeds(`
    . . . . #
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    `)
    pause(1000)
    
}

basic.forever(function on_forever() {
    progress_game(program_state)
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        let guess_number: number;
        if (program_state == "start") {
            guess_number += 1
            if (guess_number == 10) {
                guess_number = 1
            }
            
        }
        
        
    })
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        let guess_number: number;
        if (program_state == "start") {
            guess_number -= 1
            if (guess_number == 0) {
                guess_number = 9
            }
            
        }
        
        
    })
})
