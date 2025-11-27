#!/usr/bin/env python3
"""
dedupe_to_csv.py

Reads:
  - a CSV line of numbers from console
  - a CSV line of corresponding emails (TIN) from console

Produces:
  - deduped.csv with columns: sr_no,number,tin
    (keeps the first occurrence for any number)
  - prints to console a list of deleted entries and the reason for deletion
"""

import csv
from collections import OrderedDict

def parse_csv_line(line: str):
    """Split by comma and strip whitespace; keep entries even if empty string."""
    return [part.strip() for part in line.split(",")]

def main():
    print("Enter numbers as CSV (e.g. 98765, +91-98765-43210, 012345):")
    nums_line = input().strip()
    print("Enter corresponding TINs/emails as CSV (same order, same count):")
    tins_line = input().strip()

    nums_raw = parse_csv_line(nums_line) if nums_line else []
    tins_raw = parse_csv_line(tins_line) if tins_line else []

    if len(nums_raw) != len(tins_raw):
        print(f"Warning: you entered {len(nums_raw)} numbers and {len(tins_raw)} TINs.")
        print("Pairing up to the smaller length and ignoring extras.")
    n = min(len(nums_raw), len(tins_raw))

    # OrderedDict to preserve first-seen order of numbers
    kept = OrderedDict()   # number_str -> tin_str
    deleted = []           # list of dicts with details about deletions
    seen_pairs = set()     # to mark exact pair duplicates if needed

    for idx in range(n):
        num = nums_raw[idx].strip()
        tin = tins_raw[idx].strip()
        # skip rows where both empty
        if num == "" and tin == "":
            deleted.append({
                "index": idx+1,
                "number": num,
                "tin": tin,
                "reason": "both_empty - skipped"
            })
            continue

        pair = (num, tin)

        # If this number hasn't been seen yet, keep it (first occurrence wins)
        if num not in kept:
            kept[num] = tin
            seen_pairs.add(pair)
        else:
            # number already seen before
            first_tin = kept[num]
            if tin == first_tin:
                # exact duplicate pair (same number and same tin)
                deleted.append({
                    "index": idx+1,
                    "number": num,
                    "tin": tin,
                    "reason": "duplicate_pair - same number & same tin as earlier"
                })
            else:
                # same number but different tin: we keep the earlier tin
                deleted.append({
                    "index": idx+1,
                    "number": num,
                    "tin": tin,
                    "reason": f"duplicate_number - earlier tin kept: '{first_tin}'"
                })

    # Write deduped.csv
    output_filename = "deduped.csv"
    with open(output_filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sr_no", "number", "tin"])
        sr = 1
        for num, tin in kept.items():
            writer.writerow([sr, num, tin])
            sr += 1

    # Print summary and deleted list
    print("\n=== Deduplication complete ===")
    print(f"Output file written: {output_filename}")
    print(f"Total input pairs considered: {n}")
    print(f"Total kept unique numbers: {len(kept)}")
    print(f"Total deleted/ignored entries: {len(deleted)}\n")

    if deleted:
        print("Deleted / ignored entries (in order encountered):")
        # Print a neat table-like listing
        print(f"{'pos':>4}  {'number':<20}  {'tin':<30}  {'reason'}")
        print("-" * 80)
        for d in deleted:
            pos = d["index"]
            number = d["number"] or "<empty>"
            tin = d["tin"] or "<empty>"
            reason = d["reason"]
            print(f"{pos:>4}  {number:<20}  {tin:<30}  {reason}")
    else:
        print("No entries were deleted.")

if __name__ == "__main__":
    main()
