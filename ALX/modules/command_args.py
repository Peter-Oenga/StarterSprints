import sys
arg_len = len(sys.argv) - 1

if arg_len == 0:
    print("{} arguments.".format(arg_len))
elif arg_len == 1:
    print("{} argument:".format(arg_len))
    print("{}: {}".format(arg_len , sys.argv[arg_len]))
else:
    print("{} arguments:".format(arg_len))
    for arg in range(arg_len):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))