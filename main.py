def get_input_number():

    def on_button_pressed_a():
        pass
    input.on_button_pressed(Button.A, on_button_pressed_a)
    pass


def checkGuess():
    guess_number = int(input('Guess a number\n'))

        if guess_number < computer_number:
            print("Your guess is too low, try again.\n")

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


basic.show_leds("""
    # . # . #
        . . . . .
        . # . # .
        . . . . .
        . # # # .
""")

def on_forever():
    doSomething()
basic.forever(on_forever)
