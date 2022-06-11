myTimer = 6
timerTimeout = 1

def on_run_in_parallel():
    while True:
        pause(4000)
        control.raise_event(myTimer, timerTimeout)
control.run_in_parallel(on_run_in_parallel)

control.wait_for_event(myTimer, timerTimeout)
print("Timer timeout")
control.wait_for_event(myTimer, timerTimeout)
print("Timer timeout")

program_state = "start"
computer_number = 0

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
    current_state = "start"
    computer_number = randint(1, 9)
    basic.clear_screen()
    basic.show_string("guess")
    pass

def get_input():
    pass

def check_number(guess_number):    

        if guess_number < computer_number:
            print(">.\n")

        if guess_number > computer_number:
            print("Your guess is too high, try again.\n")

        if guess_number == computer_number:
            print("Congratulations")
            number_flag = True
            break

        if counter >= number_guesses:
            print("Sorry you ran out of guesses, please try again.\n")
            number_flag = True
    pass

def end():
    pass

def on_button_pressed_a():
    pass

def on_button_pressed_b():
    pass




def on_forever():
    progress_game(program_state)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)

basic.forever(on_forever)