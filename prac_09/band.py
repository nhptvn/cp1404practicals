class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        return self.musicians.append(musician)

    def play(self):
        lines = []
        for musician in self.musicians:
            if musician.instruments:
                lines.append(f"{musician.name} is playing {musician.instruments[0]}")
            else:
                lines.append(f"{musician.name} needs an instrument!")
        return "\n".join(lines)




