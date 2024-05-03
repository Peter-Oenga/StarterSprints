def max_integer(my_list=[]):
    if my_list != []:
        largest_num = my_list[0]

        for i in my_list[1:]:
            if i > largest_num:
                largest_num = i
        return largest_num
    
    else:
        return None

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))