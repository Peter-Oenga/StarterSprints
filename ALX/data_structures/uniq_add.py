"""
Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
"""

def uniq_add(my_list=[]):
    sum = 0

    added_items = set()

    for item in my_list:
        if item not in added_items:
            sum += item
            added_items.add(item)
    
    return sum

my_list = [1, 4, 2, 5,2, 3, 1]
result = uniq_add(my_list)
print("Result: {:d}".format(result))