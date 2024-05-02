def print_matrix_integer(matrix = [[]]):
    for row in matrix:
        for i in range(len(row)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(row[i]), end="")
        print()

# Test cases
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
