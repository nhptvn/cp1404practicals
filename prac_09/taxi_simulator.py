from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_taxi = None
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif menu_choice == "d":
            bill_to_date = drive(current_taxi, bill_to_date)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        menu_choice = input(MENU).lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, current_taxi):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice > 2 and not int:
        print("Invalid taxi choice")
        taxi_choice = int(input("Choose taxi: "))
    current_taxi = taxis[taxi_choice]
    return current_taxi


def drive(current_taxi, bill_to_date):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill_to_date
    current_taxi.start_fare()
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    bill_to_date += trip_cost
    return bill_to_date


main()
