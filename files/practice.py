import os
import random
import re


# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
def is_contain_twinkle():
    with open("poems.txt") as file:
        for line in file:
            if "twinkle" in line.lower():
                return True
    return False


# print(is_contain_twinkle())


#  The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score


def run_game():
    # Ensure file exists
    if not os.path.exists("Hi-score.txt"):
        with open("Hi-score.txt", "w") as file:
            file.write("0")

    def game():
        # Simulate playing the game
        return random.randint(0, 100)  # Replace with actual game logic

    def update_score(new_score):
        with open("Hi-score.txt", "r") as file:
            content = file.read().strip()
            current_high = int(content) if content else 0

        if new_score > current_high:
            with open("Hi-score.txt", "w") as file:
                file.write(str(new_score))

    # Run game and update score
    score = game()
    update_score(score)
    print(f"Your score: {score}")


# run_game()


# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
# save it to multiplication-table/table{2-20}.txt


def generate_multiplication_tables():
    """
    Generates multiplication tables from 2 to 20 and writes each to a file
    inside the 'multiplication-table' folder.
    """
    # if multiplication-table folder doesn't exist, create it
    output_folder = "multiplication-table"

    # https://chatgpt.com/c/680bb1d8-d4c4-8011-ad79-c9f194e05f5e
    # approach 1
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # or approach 1 => python has a shortcut
    # os.makedirs(output_folder, exist_ok=True)

    for number in range(2, 21):
        with open(f"{output_folder}/table{number}.txt", "w") as table_file:
            for i in range(1, 11):
                table_file.write(f"{number} * {i} = {number * i}\n")


# generate_multiplication_tables()


# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.


def change_donkey_to_hash():
    old_word = "donkey"
    new_word = "####"
    file_path = "donkey.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

    # # Replace the word in each line
    # for i in range(len(lines)):
    #     if old_word in lines[i]:
    #         lines[i] = lines[i].replace(old_word, new_word)

    # Replace all occurrences of 'donkey' (case insensitive) with '####'
    for i in range(len(lines)):
        lines[i] = re.sub(old_word, new_word, lines[i], flags=re.IGNORECASE)

    # Write the modified content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)
    print("Replacement complete.")


# change_donkey_to_hash()

# 5. Repeat program 4 for a list of such words to be censored.
censored_words = ["donkey", "ass", "monkey", "elephant"]


def remove_censored_words():
    file_path = "comment.txt"
    with open("comment.txt", "r") as file:
        lines = file.readlines()

    # replace censored words with "****"
    for i in range(len(lines)):
        for word in censored_words:
            lines[i] = re.sub(word, "****", lines[i], flags=re.IGNORECASE)

    # Write the modified content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)
    print("Replacement complete.")


# remove_censored_words()


# 6. Write a program to mine a log file and find out whether it contains ‘python’.
def is_word_python_present():
    with open("python-poem.txt", "r") as file:
        for line in file:
            if "python" in line.lower():
                return "Found!"
        return "Not found!"


# print(is_word_python_present())


# 7. Write a program to find out the line number where python is present from ques 6.
def word_python_in_which_line():
    line_number = 0
    with open("python-poem.txt", "r") as file:
        for line in file:
            line_number += 1
            if "python" in line.lower():
                return line_number
        return "Not found!"


# print(word_python_in_which_line())


def copy_text_file():
    source_file = "this.txt"
    destination_file = "copy_of_this.txt"

    if not os.path.exists(source_file):
        return f"{source_file} file is not exists"
    with open(source_file, "r") as src:
        content = src.read()

    with open(destination_file, "w") as dest:
        dest.write(content)

    return "Success!"


# print(copy_text_file())


# 9. Write a program to find out whether a file is identical & matches the content of another file
def check_identical_file(file1, file2):
    # check is file exits
    if not os.path.exists(file1) or not os.path.exists(file2):
        return f"{file1} or {file2} doesn't exits."

    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = [line.rstrip() for line in f1.readlines()]
        lines2 = [line.rstrip() for line in f2.readlines()]

    # match
    return lines1 == lines2


"""Straight answer:

Because newlines (\n) are real characters in a file.
If one file has extra \n at the end, they are not byte-for-byte identical.
"""

# print(check_identical_file("file1.txt", "file2.txt"))


# 10. Write a program to wipe out the content of a file using python.
def wipe_out_content():
    with open("comment.txt", "w") as f:
        f.write("")


# wipe_out_content()


# 11. Write a python program to rename a file to “renamed_by_ python.txt.