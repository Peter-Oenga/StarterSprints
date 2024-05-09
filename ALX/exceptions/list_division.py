"""
Write a function that divides element by element 2 lists.

Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists
Returns a new list (length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my_list_1 or my_list_2 is too short
print: out of range
You have to use try: / except: / finally:
You are not allowed to import any module
"""

def list_division(my_list_1, my_list_2, list_length):
    results = []
    for x, y in zip(my_list_1[:list_length], my_list_2[:list_length]):
        try:
            result = x / y
            results.append(result)
        except (TypeError, ValueError):
            print("wrong type")
            results.append(0)
        except ZeroDivisionError:
            print("division by 0")
            results.append(0)

    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("Out of range")
        
    return results

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)