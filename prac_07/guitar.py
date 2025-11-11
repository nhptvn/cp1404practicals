class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation."""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Return age of guitar."""
        return 2025 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return true if guitar is older than the other guitar."""
        return self.year < other.year
