x = [
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # MATRIX 0
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # MATRIX 1
    [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # MATRIX 2
    [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # MATRIX 3
    [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # MATRIX 4
    [[6, 6, 6], [6, 6, 6], [6, 6, 6]],  # MATRIX 5
    [[7, 7, 7], [7, 7, 7], [7, 7, 7]],  # MATRIX 6
    [[8, 8, 8], [8, 8, 8], [8, 8, 8]],  # MATRIX 7
    [[9, 9, 9], [9, 9, 9], [9, 9, 9]]   # MATRIX 8
]

# Define the dimensions of the blocks
block_rows = 3
block_cols = 3

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
