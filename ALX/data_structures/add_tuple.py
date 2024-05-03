def add_tuple(tuple_a=(), tuple_b=()):
    #Ensure that the elements are 2
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    #Add the elements to their corresponding tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result

tuple_a = (1, 23)
tuple_b = (24, 2)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (25, )))