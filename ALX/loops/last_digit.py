import random

# Generate a random number
number = random.randint(-10000, 10000)

# Get the last digit, including the sign
last_digit = abs(number) % 10

# Check if the number is negative
if number < 0:
    # Include the sign in the last digit
    last_digit = -last_digit

# Determine the message based on the last digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
