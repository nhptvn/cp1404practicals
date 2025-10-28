COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50",
                  "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antique White": "#faebd7", "Apricot": "#fbceb1",
                  "Aqua": "#00ffff"}
colour = input("Colour: ").title()
while colour != "":
    try:
        print(f"For {colour} code: {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour code.")
    colour = input("Colour: ").title()
