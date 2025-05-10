letter = """
Dear <|Name|>,
You are selected!
<|Date|>"""


def fill_in_the_blanks():
    name = input("Suggest a name: ")
    date = input("Suggest a date: ")
    
    filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
    return filled_letter

print(fill_in_the_blanks())

