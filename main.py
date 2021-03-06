msecs = control.millis()
computer_number = 0
guess_number = 1
button_pressed = False
program_options = ["start","get_input","check_number","end"]
program_state = program_options[0]

led_blank = """
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
"""

led_smile = """
. . . . .
. # . # .
. . . . .
# . . . #
. # # # .
"""

led_higher = """
. . # . .
. # . # .
# . . . #
# . . . #
# . . . #
"""

led_lower = """
# . . . #
# . . . #
# . . . #
. # . # .
. . # . .
"""

led_congratulations = """
. . . . #
. . . . #
. . . # .
# . # . .
. # . . .
"""






def progress_game():
    global program_state, program_options
    if program_state == program_options[0]:
        start_game()
    elif program_state == program_options[1]:
        get_input()
    elif program_state == program_options[2]:
        check_number()
    elif program_state == program_options[3]:
        end()


def start_game():
    global program_state, program_options, computer_number, button_pressed, msecs
    program_state = program_options[0]
    computer_number = randint(1, 9)
    basic.clear_screen()
    basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
    msecs = control.millis()
    while True:
        msecs_diff = control.millis() - msecs
        if button_pressed or msecs_diff > 1000:
            break

    program_state = program_options[1]
    basic.clear_screen()
    basic.show_string("guess")
    pass


def get_input():
    global program_state, program_options, guess_number, msecs
    basic.clear_screen()    
    msecs = control.millis()
    while True:
        msecs_diff = control.millis() - msecs
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        basic.show_number(guess_number)
        hertz_offset = 840 - int(((5000-msecs_diff)/5000)*400)
        time_offset = 1000 - int(((5000-(5000-msecs_diff))/5000)*500)
        music.play_tone( hertz_offset , time_offset)
        msecs_diff = control.millis() - msecs
        if msecs_diff > 5000:
            break

    program_state = program_options[2]
    pass


def on_button_pressed_a():
    global program_state, button_pressed, guess_number, program_options, msecs
    button_pressed = True
    if program_state == program_options[1]:
        msecs = control.millis()
        guess_number -=1
        if guess_number == 0:
                guess_number = 9
    pass

def on_button_pressed_b():
    global program_state, button_pressed, guess_number, program_options, msecs
    button_pressed = True
    if program_state == program_options[1]:
        msecs = control.millis()
        guess_number +=1
        if guess_number == 10:
            guess_number = 1
    pass
    



def check_number():
    global program_state, program_options, guess_number, computer_number
    if guess_number > computer_number:
        basic.show_leds("""
        . . # . .
        . # . . .
        # . . . .
        . # . . .
        . . # . .
        """)
        pause(1000)
        program_state = program_options[1]

    if guess_number < computer_number:
        basic.show_leds("""
        . . # . .
        . . . # .
        . . . . #
        . . . # .
        . . # . .
        """)
        pause(1000)
        program_state = program_options[1]

    if guess_number == computer_number:
        program_state = program_options[3]
    
    pass


def end():
    global program_state, button_pressed, program_options
    button_pressed = False
    basic.show_leds("""
    . . . . #
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    """)
    pause(1000)
    program_state = program_options[0]
    pass



def on_forever():
    progress_game()    

basic.forever(on_forever)