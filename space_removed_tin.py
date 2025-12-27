import re

# Take CSV input
user_input = input("Enter comma-separated values: ")

# Split into list
values = [v.strip() for v in user_input.split(",")]

clean_numbers = []
not_convertible = []

for original in values:
    # Remove spaces
    no_space = original.replace(" ", "")
    
    # Extract digits only
    digits = re.sub(r"\D", "", no_space)
    
    clean_numbers.append(digits)
    
    # If no digits OR original had letters/symbols that were removed, track it
    if digits == "" or not original.replace(" ", "").isdigit():
        not_convertible.append(original)

# Join cleaned numbers into CSV
csv_output = ",".join(clean_numbers)

print("\nCleaned CSV output:")
print(csv_output)

print("\nInputs that cannot be fully converted to numbers:")
for item in not_convertible:
    print(item)
