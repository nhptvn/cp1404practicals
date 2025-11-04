from prac_06.guitar import Guitar

# Testing part of the question
guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
other_guitar = Guitar("Other Guitar", 2012, 123.12)
print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected 13. Got {other_guitar.get_age()}")

print(f"{guitar.name} is_vintage - Expected True. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage - Expected False. Got {other_guitar.is_vintage()}")


