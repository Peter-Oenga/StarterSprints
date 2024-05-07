"""
Problem statement
Write a function that returns a set of all elements present in only one set.

solution -  I found two solution methods for this problem
1.) Use set ^
2.) symmetric_difference()
"""

def only_diff_elements(set_1, set_2):
    different_elements = set_1 ^ set_2
    return different_elements


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
