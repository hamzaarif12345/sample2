# Ask user to enter comma-separated numbers
user_input = input("Enter comma-separated numbers: ")

# Split and clean
numbers = [num.strip() for num in user_input.split(",")]

# Count frequency
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

# Calculate statistics
single_count = sum(1 for count in frequency.values() if count == 1)
duplicate_count = sum(1 for count in frequency.values() if count > 1)

# Print statistics
print("\n--- Statistics ---")
print(f"Total unique numbers: {len(frequency)}")
print(f"Numbers with single occurrence: {single_count}")
print(f"Numbers with duplicates (more than 1 time): {duplicate_count}")

# Print numbers that appear more than once
print("\n--- Numbers occurring more than once ---")
for num, count in frequency.items():
    if count > 1:
        print(f"{num} → {count} times")
