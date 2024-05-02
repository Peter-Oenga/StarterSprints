def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        # create a new list to store a value
        new_list = my_list[:]

        #Replace the element at a specified index
        new_list[idx] = new_element
        
        return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)