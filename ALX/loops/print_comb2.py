
for i in range(0, 100):
    if i < 10:
        print(f"0{i}, ", end="")
    elif i == 99:
        print(f"{i}", end="")
    else:
        print(f"{i}, ", end="")
