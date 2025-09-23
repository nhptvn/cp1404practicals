"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get a score and print the result."""
    user_score = float(input("Enter score: "))
    result = determine_result(user_score)
    print(result)
    random_score = random.randint(0, 100)
    result = determine_result(random_score)
    print(result)


def determine_result(score):
    """Determine a result based on given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
