from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes higher costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialised a SilverServiceTaxi instance based on parent class Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of SilverServiceTaxi based on parent class Taxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for a trip based on parent class Taxi"""
        return self.flagfall + super().get_fare()
