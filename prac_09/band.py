class Band:
    """Represent a Band class."""
    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band class."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add musician into musicians of the band."""
        return self.musicians.append(musician)

    def play(self):
        """Play and instrument if a musician has an instrument."""
        lines = []
        for musician in self.musicians:
            if musician.instruments:
                lines.append(f"{musician.name} is playing {musician.instruments[0]}")
            else:
                lines.append(f"{musician.name} needs an instrument!")
        return "\n".join(lines)




