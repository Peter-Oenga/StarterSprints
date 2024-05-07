"""
Write a function that returns a set of common elements in two sets.
"""
def common_elements(set_1, set_2):
    common_values = set_1.intersection(set_2)
    return common_values

set_1 = { "Python", "C", "Javascript", "21, 12, 1" }
set_2 = { "Bash", "C", "Ruby", "Perl" ," 1, 12, 23 "}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))