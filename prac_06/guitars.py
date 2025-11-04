from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        guitar_name = input("Name: ")

    if len(guitars) > 0:
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            else:
                vintage_string = ""
            print(f"Guitar {i}: {guitar.name:>20} {guitar.year}, worth ${guitar.cost:10.2f} {vintage_string}")
    else:
        print("No guitars were entered.")


main()