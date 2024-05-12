#!/usr/bin/python3

def remove_char_at(str, n):
    str1 = ""
    for x in range(len(str)):
        if x != n:
            str1 += str[x]
    return str1


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))