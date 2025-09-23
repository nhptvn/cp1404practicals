def main():
    """Run the main-menu of the program."""
    score = get_valid_score()
    choice = input("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>> ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            result = determine_result(score)
            print(result)
        elif choice == "s":
            print("*" * score)
        else:
            print("Invalid choice")
        choice = input("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\n>>> ").lower()
    print("Farewell.")


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


def get_valid_score():
    """Get a score from the user and determine if it is valid."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Score: "))
    return score


main()
