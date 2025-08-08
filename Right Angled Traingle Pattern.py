rows = 4
for i in range(1, rows + 1):
    # spaces
    print(" " * (rows - i), end="")
    # stars with spaces
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
