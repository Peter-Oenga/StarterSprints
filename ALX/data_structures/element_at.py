def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return "None"
    else:
        for i in my_list:
            if i == idx:
                return my_list[i]


my_list = [1, 2, 3, 4, 5]
idx = 2
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))