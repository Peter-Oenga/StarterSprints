def no_c(my_string):
    result = ''

    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

print(no_c("My school"))