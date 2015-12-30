#!/usr/bin/env python3

import random


def guess_the_number():
    guess = input(str(counter) + ": What is your guess? ")

    try:
        guess = int(guess)
    except Exception:
        print("Your guess was not an integer. Please guess again")
        return False

    if not 0 < guess <= 100:
        print("Guess is out of range!")
        return False
    elif guess == number:
        print("You've guessed the number correctly! Hurray!!")
        exit()
    else:
        if guess < number:
            print("Guess is too low!")
        elif guess > number:
            print("Guess is too high!")


def main():
    global counter
    counter = 1

    while counter <= 7:
        if guess_the_number() is False:
            continue
        counter += 1

    print("unfortunately, you've exhausted your 7 guesses.")
    print(" The correct number was", number)


if __name__ == "__main__":
    number = random.randint(1, 100)
    # Why am I allowed to define number [var] outside of main, but can't
    # define counter outside of main?
    main()
