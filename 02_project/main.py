import random


def generate_number():
    return random.randint(1, 100)


def get_user_guess():
    """Get a guess from the user and validate it.

    The function will keep prompting the user until a valid number is provided.
    The number must be within the range of 1 to 100.

    Returns:
        int: The valid guess from the user.
    """
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def choose_difficulty():
    choice = input(
        "Choose difficulty\nType 'e' for easy (10 lives), 'h' for hard (5 lives): ").lower()
    return 10 if choice != 'h' else 5


def play_game():
    number = generate_number()
    lives = choose_difficulty()
    attempts = 0

    while lives > 0:
        guess = get_user_guess()
        attempts += 1

        if guess > number:
            print("Lower number please.")
        elif guess < number:
            print("Higher number please.")
        else:
            print(
                f"Correct! You guessed the number {number} in {attempts} attempts.")
            return

        lives -= 1
        print(f"Lives remaining: {lives}\n")

    print(f"Game over! The correct number was {number}.")


def main():
    """
    Runs the game in a loop, prompting user to play again after each round.
    """

    while True:
        play_game()
        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break


main()


"""
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.
"""
