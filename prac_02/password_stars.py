def main():
    min_length = 8
    password = get_password(min_length)
    print('*' * len(password))


def get_password(min_length):
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    return password


main()
