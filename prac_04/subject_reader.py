"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_information = load_data(FILENAME)
    print_subject(subject_information)


def load_data(filename=FILENAME):
    """Read subject from file formatted like: subject,lecturer,number of students."""
    things = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        things.append(parts)
    input_file.close()
    return things


def print_subject(subject_information):
    for subject in subject_information:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
