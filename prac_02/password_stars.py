def main():
    """Print stars based on the length of a password."""
    min_length = 8
    password = get_valid_password(min_length)
    print('*' * len(password))


def get_valid_password(min_length):
    """Get a password from user and check if it is valid"""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password


main()
