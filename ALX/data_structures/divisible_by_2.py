def divisible_by_2(my_list=[]):
    is_divisible = []

    for num in my_list:
        if num % 2 == 0:
            is_divisible.append(True)
        else:
            is_divisible.append(False)

    return is_divisible
        
            
my_list = [0, 2, 5, 3, 9, 5, 6]
list_result = divisible_by_2(my_list)

#Initialize the positional i
i = 0

#Check to see if the value at position i is not bigger than the length of the list
while i < len(my_list):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i+= 1