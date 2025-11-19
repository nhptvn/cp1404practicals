from prac_09.unreliable_car import UnreliableCar


def main():
    """Drive reliable car program."""
    reliable_car = UnreliableCar("Toyota", 10000, 90)
    reliable_car.drive(50)
    unreliable_car = UnreliableCar("Nissan", 10000, 10)
    unreliable_car.drive(50)
    for i in range(50, 55):
        print(f"{reliable_car.name} drove {reliable_car.drive(i)}")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}")
    print(reliable_car)  # More on the odometer means driven more which means better reliability
    print(unreliable_car)


main()

