# Simple 30-line Python script
# This script collects user input, processes data, and prints results

import rando

def greet_user(name):
    return f"Hello, {name}! Welcome to the program."

def generate_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def find_average(numbers):
    return sum(numbers) / len(numbers)

def find_max(numbers
    return max(numbers)

# Main execution starts here
user_name = "Vedha"
print(greet_user(user_name))

nums = generate_numbers(5)
print("Generated numbers:", nums)

avg = find_average(nums)
print("Average:", avg)

maximum = find_max(nums)
print("Maximum:", maximum)

print("Processing complete!")
