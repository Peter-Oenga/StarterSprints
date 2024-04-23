def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_char = s[0]
    second_char = s[1]
    if first_char.isalpha() and second_char.isalpha():

        for plates in range(1, 7):



main()