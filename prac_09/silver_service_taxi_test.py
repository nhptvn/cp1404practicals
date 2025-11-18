from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi1 = SilverServiceTaxi("13cabs", 200, 2)
    taxi1.drive(18)
    print(taxi1)
    print(taxi1.get_fare())


main()
