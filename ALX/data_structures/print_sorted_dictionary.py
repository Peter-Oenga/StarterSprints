

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
         print(key,":", value)
        

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)