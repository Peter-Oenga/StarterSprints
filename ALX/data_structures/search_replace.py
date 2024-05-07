"""
Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
"""

def search_replace(my_list, search, replace):
    new_list = [replace if item == search else item for item in my_list]
    return new_list
my_list = [1, 1, 1, 4, 5, 4, 2, 1, 1, 1, 89]
new_list = search_replace(my_list, 1, 89)

print(new_list)
print(my_list)