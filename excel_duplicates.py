# duplicate_finder.py
# Ask user for CSV of numbers and CSV of corresponding emails.
# Output:
#  - duplicate (number, email) pairs
#  - duplicate numbers (with counts and associated emails)
#  - duplicate emails (with counts and associated numbers)

import re
from collections import Counter, defaultdict

def normalize_number(s: str) -> str:
    """Normalize numeric-like strings: remove spaces, dashes, parentheses.
       Keeps leading + if present. If all digits except leading +, keep that."""
    s = s.strip()
    if not s:
        return ""
    # allow leading +, remove other nondigit chars
    if s.startswith("+"):
        body = re.sub(r"[^\d]", "", s[1:])
        return "+" + body if body else s
    else:
        return re.sub(r"[^\d]", "", s)

def normalize_email(s: str) -> str:
    """Basic normalization for emails: lowercasing and stripping spaces."""
    return s.strip().lower()

def parse_csv_line(line: str):
    """Split by comma and strip each part. Keeps empty strings for empties."""
    return [part.strip() for part in line.split(",")]

def main():
    print("Enter numbers as CSV (e.g. 98765, +1-800-234-5678, 012345):")
    num_line = input().strip()
    print("Enter corresponding emails as CSV (same order, same count):")
    mail_line = input().strip()

    nums_raw = parse_csv_line(num_line) if num_line else []
    mails_raw = parse_csv_line(mail_line) if mail_line else []

    if len(nums_raw) != len(mails_raw):
        print(f"Warning: you entered {len(nums_raw)} numbers and {len(mails_raw)} emails.")
        print("The script will pair entries up to the smaller length and ignore extra items.")
    n = min(len(nums_raw), len(mails_raw))

    pairs = []
    for i in range(n):
        nr = normalize_number(nums_raw[i])
        mr = normalize_email(mails_raw[i])
        # skip entirely empty rows
        if nr == "" and mr == "":
            continue
        pairs.append((nr, mr))

    if not pairs:
        print("No valid pairs to analyze (empty input).")
        return

    # Find duplicate pairs
    pair_counts = Counter(pairs)
    duplicate_pairs = {p: c for p, c in pair_counts.items() if c > 1}

    # Find duplicate numbers and map to emails/indices
    number_map = defaultdict(list)   # number -> list of emails where it occurred
    number_counts = Counter()
    email_map = defaultdict(list)    # email -> list of numbers where it occurred
    email_counts = Counter()

    for (num, mail) in pairs:
        number_counts[num] += 1
        number_map[num].append(mail)
        email_counts[mail] += 1
        email_map[mail].append(num)

    duplicate_numbers = {num: number_counts[num] for num in number_counts if number_counts[num] > 1}
    duplicate_emails = {mail: email_counts[mail] for mail in email_counts if email_counts[mail] > 1}

    # Output results
    print("\n=== Results ===\n")

    # 1) Duplicate (number, email) pairs
    if duplicate_pairs:
        print("Duplicate (number, email) pairs (pair : count):")
        for (num, mail), cnt in duplicate_pairs.items():
            print(f"  - ({num!s}, {mail!s}) : {cnt} times")
    else:
        print("No duplicate (number, email) pairs found.")

    print()  # blank line

    # 2) Duplicate numbers
    if duplicate_numbers:
        print("Duplicate numbers (number : count) and associated emails:")
        for num, cnt in duplicate_numbers.items():
            emails = number_map.get(num, [])
            # unique emails shown
            unique_emails = sorted(set(emails))
            print(f"  - {num} : {cnt} times -> emails: {unique_emails}")
    else:
        print("No duplicate numbers found.")

    print()

    # 3) Duplicate emails
    if duplicate_emails:
        print("Duplicate emails (email : count) and associated numbers:")
        for mail, cnt in duplicate_emails.items():
            nums = email_map.get(mail, [])
            unique_nums = sorted(set(nums))
            print(f"  - {mail} : {cnt} times -> numbers: {unique_nums}")
    else:
        print("No duplicate emails found.")

if __name__ == "__main__":
    main()
