import sys

arg_len = len(sys.argv) - 1

sum = 0
for arg in range(1, arg_len + 1):
    sum += int(sys.argv[arg])
print(sum)