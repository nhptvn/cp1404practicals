"""
Emails
Estimate: 15 mins
Actual: 33 mins
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name_from_email(email)
        name_confirmation = input(f"Is your name {full_name}? (Y/n) ").lower()
        if name_confirmation == "n":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name_in_email = email.split("@")[0]
    name_part = name_in_email.split(".")
    full_name = " ".join(name_part).title()
    return full_name


main()
