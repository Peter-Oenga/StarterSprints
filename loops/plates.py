my_string = "1ello World"

if len(my_string) >= 2:
    first_two = my_string[:2]  # Get the first two characters
    if first_two.isalpha():
        print("The first two characters are both strings.")
    else:
        print("The first two characters are not both strings.")
else:
    print("The string is too short to check the first two characters.")
