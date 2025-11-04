from guitar import Guitar


def main():
    """Guitars main program."""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    get_guitar(guitars)
    display_guitars(guitars)
    save_guitars(guitars)
    print("Guitars saved.")


def display_guitars(guitars):
    """Display a list of guitars from oldest to newest."""
    guitars.sort()
    print("My Guitars (oldest to newest): ")
    for guitar in guitars:
        print(guitar)


def get_guitar(guitars):
    """Get a new guitar from the user."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")


def save_guitars(guitars):
    """Save guitar inputted by the user into file."""
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


main()
