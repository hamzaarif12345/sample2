import csv

CSV_FILE = "input.csv"   # your CSV file name

with open(CSV_FILE, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    for row in reader:
        # since all values are in one row, iterate each value
        for value in row:
            value = value.strip()

            open_count = value.count("(")
            close_count = value.count(")")

            # ERROR: more than one opening OR more than one closing bracket
            if open_count > 1 or close_count > 1:
                print(value)
