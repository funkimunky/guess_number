myTimer = 6
timerTimeout = 1
ticks = 0
ticks_to_wait = 30
computer_number = 0
guess_number = 0
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

def on_run_in_parallel():
    while True:
        pause(100)
        ticks += 1
        if ticks == ticks_to_wait:
            ticks = 0

control.run_in_parallel(on_run_in_parallel)


def progress_game(current_state):
    if current_state == "start":
        start_game()
    elif current_state == "get_input":
        get_input()
    elif current_state == "check_number":
        check_number()
    elif current_state == "end":
        end()


def start_game():
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
    ticks = 0
    while True:       
        if button_pressed or ticks > 10:
            ticks = 0
            break

    program_state = program_options[1]
    pass

def get_input():
    basic.clear_screen()
    basic.show_string("guess")
    ticks = 0    
    while True:
        basic.show_number(guess_number)
        if ticks > ticks_to_wait:
            break

    program_state = program_options[2]
    pass


def check_number():
    if guess_number > computer_number:
        basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        # . . . #
        """)
        pause(1000)

    if guess_number < computer_number:
        basic.show_leds("""
        # . . . #
        # . . . #
        # . . . #
        . # . # .
        . . # . .
        """)
        pause(1000)

    if guess_number == computer_number:
        program_state = program_options[3]
    
    pass


def end():
    basic.show_leds("""
    . . . . #
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    """)
    pause(1000)
    pass

def on_button_pressed_a():
    if program_state == "start":
        guess_number +=1
        if guess_number == 10:
            guess_number = 1
    pass

def on_button_pressed_b():
    if program_state == "start":
        guess_number -=1
        if guess_number == 0:
                guess_number = 9
    pass


def on_forever():
    progress_game(program_state)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)

basic.forever(on_forever)