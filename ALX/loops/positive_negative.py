import random
number = random.randint(-10, 10)

if number == 0:
    print(number, " is 0")
elif number < 0:
    print(number, " is negative")
else:
    print(number, " is positive")