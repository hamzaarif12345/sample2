#!/usr/bin/env python3
"""
find_unmatched.py

Reads two CSV lines of numbers from the console and returns unmatched numbers.

Outputs printed lists:
 - only_in_first: numbers present in first input but not in second
 - only_in_second: numbers present in second input but not in first
 - symmetric_unmatched: union of the above

Also writes unmatched.csv with columns: number, which_list
"""

import csv

def parse_csv_numbers(line: str):
    """Split by comma, strip whitespace, ignore empty tokens."""
    if not line:
        return []
    parts = [p.strip() for p in line.split(",")]
    return [p for p in parts if p != ""]

def main():
    print("Enter first CSV list of numbers (e.g. 1, 2, 45, 655):")
    a_line = input().strip()
    print("Enter second CSV list of numbers:")
    b_line = input().strip()

    a_list = parse_csv_numbers(a_line)
    b_list = parse_csv_numbers(b_line)

    # Use sets for membership comparison (keeps unique values)
    set_a = set(a_list)
    set_b = set(b_list)

    only_in_first = sorted(set_a - set_b, key=lambda x: (int(x) if x.isdigit() else x))
    only_in_second = sorted(set_b - set_a, key=lambda x: (int(x) if x.isdigit() else x))
    symmetric_unmatched = sorted((set_a ^ set_b), key=lambda x: (int(x) if x.isdigit() else x))

    # Print results
    print("\n=== Results ===\n")
    print(f"Total unique in first input : {len(set_a)}")
    print(f"Total unique in second input: {len(set_b)}\n")

    print("Numbers only in FIRST input:")
    if only_in_first:
        print(", ".join(only_in_first))
    else:
        print("<none>")

    print("\nNumbers only in SECOND input:")
    if only_in_second:
        print(", ".join(only_in_second))
    else:
        print("<none>")

    print("\nCombined unmatched numbers (symmetric difference):")
    if symmetric_unmatched:
        print(", ".join(symmetric_unmatched))
    else:
        print("<none>")

    # Write unmatched.csv
    out_file = "unmatched.csv"
    with open(out_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["number", "which_list"])
        for num in only_in_first:
            writer.writerow([num, "only_in_first"])
        for num in only_in_second:
            writer.writerow([num, "only_in_second"])

    print(f"\nWrote details to: {out_file}")

if __name__ == "__main__":
    main()
