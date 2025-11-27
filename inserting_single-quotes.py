# Program to convert CSV numbers into quoted CSV strings

csv_input = input("Enter CSV numbers: ")

# Split and clean
numbers = [x.strip() for x in csv_input.split(",") if x.strip()]

# Enclose each number in single quotes
quoted = [f"'{n}'" for n in numbers]

# Join with commas
output = ",".join(quoted) + ","

print("\nConverted output:")
print(output)
