
def contains_upper(variable):
    snake_case = " "
    for char in variable:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case
variable = input('CamelCase: ')
print("snake_case:" + contains_upper(variable))