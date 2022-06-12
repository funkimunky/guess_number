let msecs = control.millis()
let computer_number = 0
let guess_number = 1
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
function progress_game() {
    
    if (program_state == program_options[0]) {
        start_game()
    } else if (program_state == program_options[1]) {
        get_input()
    } else if (program_state == program_options[2]) {
        check_number()
    } else if (program_state == program_options[3]) {
        end()
    }
    
}

function start_game() {
    let msecs_diff: number;
    
    program_state = program_options[0]
    computer_number = randint(1, 9)
    basic.clearScreen()
    basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
    msecs = control.millis()
    while (true) {
        msecs_diff = control.millis() - msecs
        if (button_pressed || msecs_diff > 1000) {
            break
        }
        
    }
    program_state = program_options[1]
    basic.clearScreen()
    basic.showString("guess")
    
}

function get_input() {
    let msecs_diff: number;
    let hertz_offset: number;
    let time_offset: number;
    
    basic.clearScreen()
    msecs = control.millis()
    while (true) {
        msecs_diff = control.millis() - msecs
        input.onButtonPressed(Button.A, function on_button_pressed_a() {
            
            button_pressed = true
            if (program_state == program_options[1]) {
                msecs = control.millis()
                guess_number -= 1
                if (guess_number == 0) {
                    guess_number = 9
                }
                
            }
            
            
        })
        input.onButtonPressed(Button.B, function on_button_pressed_b() {
            
            button_pressed = true
            if (program_state == program_options[1]) {
                msecs = control.millis()
                guess_number += 1
                if (guess_number == 10) {
                    guess_number = 1
                }
                
            }
            
            
        })
        basic.showNumber(guess_number)
        hertz_offset = 840 - Math.trunc((5000 - msecs_diff) / 5000 * 400)
        time_offset = 1000 - Math.trunc((5000 - (5000 - msecs_diff)) / 5000 * 500)
        music.playTone(hertz_offset, time_offset)
        msecs_diff = control.millis() - msecs
        if (msecs_diff > 5000) {
            break
        }
        
    }
    program_state = program_options[2]
    
}

function check_number() {
    
    if (guess_number > computer_number) {
        basic.showLeds(`
        . . # . .
        . # . . .
        # . . . .
        . # . . .
        . . # . .
        `)
        pause(1000)
        program_state = program_options[1]
    }
    
    if (guess_number < computer_number) {
        basic.showLeds(`
        . . # . .
        . . . # .
        . . . . #
        . . . # .
        . . # . .
        `)
        pause(1000)
        program_state = program_options[1]
    }
    
    if (guess_number == computer_number) {
        program_state = program_options[3]
    }
    
    
}

function end() {
    
    button_pressed = false
    basic.showLeds(`
    . . . . #
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    `)
    pause(1000)
    program_state = program_options[0]
    
}

basic.forever(function on_forever() {
    progress_game()
})
