import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car only if reliability is higher than random amount."""
        if self.reliability > random.randint(0, 100):
            super().drive(distance)
        return distance
