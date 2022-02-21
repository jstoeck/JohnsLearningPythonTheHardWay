# setup this the script by importing the argv function
from sys import argv

# Unpack variables passed in from the Terminal using argv
script, filename = argv

# Open the file whose file name was passed in via the Terminal
txt = open(filename)

# Print a comment and read the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# Request the name of the file again as input from the user
file_again = input("Type the filename again:> ")

# Open the file whose name was input by the user so it can
# be manipulated by the program
text_again = open(file_again)

# Print the file selected by the user
print(text_again.read())

text_again.close()
