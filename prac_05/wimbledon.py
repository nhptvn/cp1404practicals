"""
Wimbledon
Estimate: 30 mins
Actual:
"""
FILENAME = "wimbledon.csv"


def main():
    records = get_record_from_file(FILENAME)
    champion_to_win, countries = process_records(records)
    print_results(champion_to_win, countries)


def print_results(champion_to_win, countries):
    for name, win in champion_to_win.items():
        print(name, win)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_record_from_file(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
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
