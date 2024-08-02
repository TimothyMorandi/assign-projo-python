"""A program to text whether a number is divisible by 5,"""
# Prompt the user to enter a number
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Check if the number is divisible by 5
if number % 5 == 0:
    print(f"Number {number} is divisible by 5: Yes")
else:
    print(f"Number {number} is divisible by 5: No")

# Check if the number is divisible by 7
if number % 7 == 0:
    print(f"Number {number} is divisible by 7: Yes")
else:
    print(f"Number {number} is divisible by 7: No")

# Check if the number is divisible by 11
if number % 11 == 0:
    print(f"Number {number} is divisible by 11: Yes")
else:
    print(f"Number {number} is divisible by 11: No")

# Check if the number is even
if number % 2 == 0:
    print(f"Number {number} is even: Yes")
else:
    print(f"Number {number} is even: No")