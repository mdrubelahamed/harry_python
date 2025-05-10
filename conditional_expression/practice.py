# 1. Write a program to find the greatest of four numbers entered by the user.
def find_greatest_of_four():
    user_numbers = []
    for i in range(4):
        number = float(input(f"Enter the number {i+1}: "))
        user_numbers.append(number)

    # Your logic fails if all numbers are negative, because max_number starts at 0.
    max_number = user_numbers[0]

    for current_number in user_numbers[1:]:
        if current_number > max_number:
            max_number = number

    return max_number


# print(find_greatest_of_four())


# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


# subject 3, each subject atleast 33% and total of 40%
def check_pass_status():
    max_marks = 100
    subject_scores = [
        float(input(f"Enter marks for Subject {i + 1} (out of {max_marks}): "))
        for i in range(3)
    ]

    for score in subject_scores:
        if score < 33:
            return "Failed: Less than 33% in one or more subjects."

    total_score = sum(subject_scores)
    overall_percentage = (total_score / (max_marks * 3)) * 100

    if overall_percentage < 40:
        return "Failed: Overall percentage is below 40%."

    return "Passed: Congratulations!"


# print(check_pass_status())


#  A spam comment is defined as a text containing following keywords: Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
SPAM_KEYWORDS = ["make a lot of money", "buy now", "subscribe this", "click this"]


def is_spam_comment(comment_text: str, spam_phrases: list) -> bool:
    """Return True if comment contains any spam phrase."""
    comment_text = comment_text.lower()
    return any(phrase in comment_text for phrase in spam_phrases)


def handle_user_comment():
    user_comment = input("Write a comment for this video: ")
    if is_spam_comment(user_comment, SPAM_KEYWORDS):
        return f"It's a spam comment, you can't post this."
    else:
        return f"You've successfully posted the comment. '{user_comment}'"


# print(handle_user_comment())


# 4. Write a program to find whether a given username contains less than 10 characters or not
def is_valid_username(username: str) -> bool:
    """Check if username has at least 10 characters."""
    return len(username) >= 10


def prompt_username():
    """Prompt for a valid username until one is entered."""
    while True:
        username = input("Enter your username: ")
        if is_valid_username(username):
            return f"Username '{username}' is valid."
        print("Username should have at least 10 characters. Try again.")


# print(prompt_username())

# 5. Write a program which finds out whether a given name is present in a list or not.
INDIAN_NAMES = [
    "Rex",
    "Rohan",
    "Rahul",
    "Amit",
    "Shivam",
    "Aisha",
    "Anjali",
    "Kavita",
    "Priya",
    "Rashmi",
]


def is_name_in_list(name: str, name_list: list) -> bool:
    """Check if name exists in the list (case-insensitive)."""
    return name.lower() in [n.lower() for n in name_list]


def prompt_for_name():
    """Prompt user for a name and check if it exists in the list."""
    name = input("Enter a name: ").strip()
    if is_name_in_list(name, INDIAN_NAMES):
        return f"Name: '{name}' is in the list."
    return "Name doesn't exist in the list."


# print(prompt_for_name())


"""
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
"""


def get_marks():
    """Get valid marks between 0 - 100."""
    while True:
        try:
            marks = int(input("Enter your marks: "))
            if 0 <= marks <= 100:
                return marks
            print("Marks should be between 0 and 100.")
        except ValueError:
            print("Please provide a valid integer for the marks.")


def get_grade():
    marks = get_marks()

    if 90 <= marks <= 100:
        return "Ex"
    elif 80 <= marks <= 89:
        return "A"
    elif 70 <= marks <= 79:
        return "B"
    elif 60 <= marks <= 69:
        return "C"
    elif 50 <= marks <= 59:
        return "D"
    else:
        return "F"


# print(get_grade())


# ******************************************************
# option 2

GRADE_SCALE = [
    (90, "Ex"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]


def get_grade(marks):
    """Return grade using reusable scale."""
    for threshold, grade in GRADE_SCALE:
        if marks >= threshold:
            return grade


"""
🧪 Example: get_grade(72)
Loop starts:

threshold = 90, grade = "Ex"
→ 72 >= 90 → ❌ No

Next:

threshold = 80, grade = "A"
→ 72 >= 80 → ❌ No

Next:

threshold = 70, grade = "B"
→ 72 >= 70 → ✅ Yes

Return "B" — loop exits immediately.
"""


# 7. Write a program to find out whether a given post is talking about “Harry” or not.
def check_in_post(name):
    post = input("Enter your post: ").lower()
    name = name.lower()
    if name in post:
        return f"This post is talking about {name.title()}."
    return f"This post is not talking about {name.title()}."


# print(check_in_post("harry"))
