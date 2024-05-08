from print_sorted_dictionary import print_sorted_dictionary

"""
Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
"""

def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        a_dictionary[key] = value * 2
    return a_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)