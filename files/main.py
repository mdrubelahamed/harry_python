# f = open("myfile.txt")
# line = f.readline()
# while line != "":
#     print(line)
#     line = f.readline()

# f.close()

# with open("myfile.txt") as f:
# for line in f.readlines():
# print(line)

# with open("myfile.txt", "a") as f:
#     for _ in range(10):
#         f.write("\nAdd")


# + - open for updating.
def open_for_updating():
    with open("sample.txt", "r+") as f:
        content = f.read()  # Read the file
        f.seek(0)  # Move to beginning
        f.write("Updated\n")  # Overwrite with new content


# open_for_updating()


def open_for_read_in_binary_mode():
    # Open a text file in binary read mode
    with open("sample.txt", "rb") as file:
        # Read binary data
        binary_content = file.read()
        print(f"Binary content:\n{binary_content}")

        print("----------------------------")
        # To see the actual text representation
        text_content = binary_content.decode("utf-8")
        print("Text content:", text_content)


# open_for_read_in_binary_mode()


def open_for_read_in_text_mode():
    # Open a text file in text read mode (same as just "r")
    with open("sample.txt", "rt") as file:
        # Read text content
        text_content = file.read()
        print("Text content:", text_content)

        # You can also read line by line
        file.seek(0)
        lines = file.readlines()
        print("Lines:", lines)


# open_for_read_in_text_mode()
