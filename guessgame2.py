#!/usr/bin/env python

import random

def main():
    """Let's play a "Guess What" game."""
    print("I am thinking of a fruit with green color.")
    
    green_fruits = [
        "avocado",
        "grapes",
        "guava",
        "kiwi",
        "noni",
        "limes",
        "pomelo",
        "pear",
        "soursop"
    ]

    x = random.choice(green_fruits)
    max_trials = 3
    trial = 0

    while trial < max_trials:
        guess = input("What fruit am I thinking of? ").lower()

        if guess in green_fruits:
                if x == guess:
                    print(f"Congratulations! You guessed it right. It's {x}!")
                    break
                else:
                    print(f"Unfortunately, that's not the correct answer.")
                    print(f"You have {max_trials - trial - 1} chances remaining.")
                    trial += 1

        else:
            print(f"Your guess is not a green fruit.' Try again with a green fruit.")
            print(f"You have {max_trials - trial} chances remaining.")

    else:
        print(f"Out of attempts. The green fruit I was thinking of is {x}.")

if __name__ == "__main__":
    main()