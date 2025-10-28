"""
Wimbledon
Estimate: 30 mins
Actual:
"""
FILENAME = "wimbledon.csv"


def main():
    """Read information from file and print information."""
    records = get_record_from_file(FILENAME)
    champion_to_win, countries = process_records(records)
    print_results(champion_to_win, countries)


def print_results(champion_to_win, countries):
    """Print the champions and countries."""
    for name, win in champion_to_win.items():
        print(name, win)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_record_from_file(filename):
    """Get record from file extracting information in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Process information in list (records) passed in and create dictionary."""
    champion_to_win = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        if record[2] not in champion_to_win:
            champion_to_win[record[2]] = champion_to_win[record[2]]
        else:
            champion_to_win[record[2]] = champion_to_win[record[2]] + 1
    return champion_to_win, countries


main()
