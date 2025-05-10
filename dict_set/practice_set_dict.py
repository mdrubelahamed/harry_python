def hindi_to_english_lookup():
    hindi_to_english = {
        "seb": "apple",
        "kela": "banana",
        "aam": "mango",
        "angur": "grape",
    }

    print("Choose an option: ")
    print("1. Look up English translation of a Hindi word")
    print("2. Exit")

    while True:
        choice = input("Enter an option: ")
        if choice == "1":
            hindi_word = input("Enter a Hindi word: ")
            translation = hindi_to_english.get(hindi_word)
            if translation:
                print(f"English translation of '{hindi_word}' is '{translation}'")
            else:
                print("Word not found in the dictionary!")
        elif choice == "2":
            break
        else:
            print("Invalid option. Please try again.")


# hindi_to_english_lookup()


# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
def get_valid_count():
    while True:
        try:
            count = int(input("How many numbers you want to input? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the count.")
    return count


def display_unique_numbers():
    count = get_valid_count()
    unique_set = set()

    for i in range(count):
        # keep asking int value until get the right value
        while True:
            try:
                number = int(input(f"Enter number {i + 1}: "))
                unique_set.add(number)
                break
            except ValueError:
                print("Invalid Input, Please enter an interger.")

    print(f"Unique Numbers: {unique_set}")


# display_unique_numbers()


# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# answer -> yes
def check_different_types_in_set():
    set1 = {18, "18"}

    if 18 in set1 and "18" in set1:
        return True
    return False


# print(check_different_types_in_set())

# s = set() s.add(20) s.add(20.0) s.add('20') # length of s after these operations?


def length_of_set():
    s = set()
    s.add(20)
    s.add(20.0)
    s.add("20")
    print(f"Length of set a is: {len(s)}")  # output : 2


# length_of_set()

# s = {}
# print(type(s)) # output: <class 'dict'>


# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.


def get_friends_language():
    while True:
        try:
            friends_count = int(input("How many friends you want to add? "))
            if friends_count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except:
            print("Please provide a right no of friends.")

    language_of_friends = {}
    for i in range(friends_count):
        name = input(f"Enter friend {i + 1} name: ")
        language = input(f"Enter friend {i + 1} language: ")

        language_of_friends[name] = language

    return language_of_friends


# call the function
# print(get_friends_language())

# If the names of 2 friends are same; what will happen to the program in problem 6?


# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1, 2]}
convert_s_to_list = list(s)
print(convert_s_to_list)
