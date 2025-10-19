#!/usr/bin/python3

# Write the algorithm
# 1. Load the input text file, and the user's message
# 2. Read each line of the input file
# 3. Replace each character of the input line with text
#   from the user's input message

# Prompt the user to the enter the message to display with the bitmap
user_message = input("Enter message to display with the bitmap: ")
msg_len = len(user_message)

# 1. Load the input text file
file_name = "bitmapworld.txt"

# Load all the lines of the input file
with open(file_name) as file:
    lines = file.readlines()


# Now lines contains all the lines in the file
for line_i, line in enumerate(lines):
    new_line = ""
    if line_i > 0 and line_i < len(lines) - 1:
        for index, ch in enumerate(line):
            msg_char = ch if ch != "\n" else ""
            if ch != "\n" and ch != " ":
                msg_char = user_message[index % msg_len]
            new_line = f"{new_line}{msg_char}"
    else:
        new_line = line[:-1]

    # Now print the line
    print(new_line)
