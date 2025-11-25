from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Drive a SilverServiceTaxi program."""
    taxi1 = SilverServiceTaxi("13cabs", 200, 2)
    taxi1.drive(18)
    print(taxi1)
    print(f"Total fare: ${taxi1.get_fare():.2f}")


main()
