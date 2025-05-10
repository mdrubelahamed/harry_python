import random


"""
Snake vs. Water: Snake wins (because it drinks water).
Water vs. Gun: Water wins (because the gun drowns).
Gun vs. Snake: Gun wins (because it shoots the snake).
Tie: If both players choose the same gesture, it's a tie.
"""


"""
✅ choice_map.get(user_input)
Safe.

If the key doesn't exist, it returns None instead of crashing.

Lets you check for invalid input before proceeding.

⚠️ choice_map[user_input]
Unsafe.

If the user types something like "x", it throws a KeyError and the program crashes.
"""
# ------------------------------------------------------


def snake_water_gun():
    choice_map = {"s": "snake", "w": "water", "g": "gun"}

    # Winnning combination
    outcome = {
        ("snake", "water"): "You win",
        ("water", "gun"): "You win",
        ("gun", "snake"): "You win",
    }

    user_input = input("Enter your choice ('s'=snake, 'w'=water, 'g'=gun): ").lower()
    user_choice = choice_map.get(user_input)  # safe

    if user_choice is None:
        return "Invalid input."

    # run if user chose a valid input
    computer_choice = random.choice(list(choice_map.values()))
    print(f"\nComputer chose: {computer_choice}\nYou chose: {user_choice}")

    # compare
    if user_choice == computer_choice:
        return "It's a tie."

    return outcome.get((user_choice, computer_choice), "You lose")


# print(snake_water_gun())
