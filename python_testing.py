def print_matrices(x):
    # Define the dimensions of the blocks

    for j in range(0,3):
        print()
        for h in range(0,3):
            print(end=" ")
            for i in range(0,3):
                print(x[h][j][i], end="")
    print()

    for j in range(0,3):
        print()
        for h in range(3,6):
            print(end=" ")
            for i in range(0,3):
                print(x[h][j][i], end="")
    print()

    for j in range(0,3):
        print()
        for h in range(6,9):
            print(end=" ")
            for i in range(0,3):
                print(x[h][j][i], end="")
    print()