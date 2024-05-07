"""
Write a function that returns the number of keys in a dictionary
"""

def number_keys(a_dictionary):
    no_keys = len(a_dictionary)
    return no_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))