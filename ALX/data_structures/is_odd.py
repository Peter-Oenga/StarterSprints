"""
Write a function that receives a list and a function. The function received will return True or False if a List value is odd
"""
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def func(lis, fun):
    empty_list = []

    for i in lis:
        if fun(i):
            empty_list.append(i)

    return empty_list

aList = range(1, 20)
print(func(aList, is_it_odd))
