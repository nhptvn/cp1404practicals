from prac_09.taxi import Taxi


def main():
    taxi1 = Taxi("Prius 1", 100)
    taxi1.drive(40)
    print(taxi1)
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)


main()
