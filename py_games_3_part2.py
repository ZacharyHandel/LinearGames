#This is the main file for Linear Games 3
import random

#Create matrices variable that contains all if the matrices we want to work upon
matrices = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]

#FUNCITONS******************************************************************************
def input_matrix(matrix):
    for i in range(9):
        for j in range(3):
            for k in range(3):
                while True:
                    try:
                        value = int(input(f"Enter a value for matrix[{i}][{j}][{k}]: "))
                        if 0 <= value <= 2:
                            matrix[i][j][k] = value
                            break
                        else:
                            print("Please input an integer between 0-2")
                    except ValueError:
                        print("Please input an integer between 0-2")

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

def print_matrix(matrix):
    for row in matrices[matrix]:
        print(' '.join(map(str, row)))


def check_win(matrices):
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if matrices[i][j][k] != 0:
                    return False
    return True

def fill_random(matrices):
    #Fill matrices randomly
    # Fill each matrix with random values
    for i in range(9):
        matrix = [[random.randint(0, 2) for _ in range(3)] for _ in range(3)]
        matrices.append(matrix)

def fill_zeros(matrices):
    for i in range(9):
        matrix = [[0 for _ in range(3)] for _ in range(3)]
        matrices.append(matrix)

def solvable(matrix):
    value = 0
    presses_needed = [0,0,0,0,0,0,0,0,0]
    possible_presses = [[1,1,0,1,1,0,0,0,0],
                        [1,1,1,0,0,0,0,0,0],
                        [0,1,1,0,1,1,0,0,0],
                        [1,0,0,1,0,0,1,0,0],
                        [0,1,0,1,1,1,0,1,0],
                        [0,0,1,0,0,1,0,0,1],
                        [0,0,0,1,1,0,1,1,0],
                        [0,0,0,0,0,0,1,1,1],
                        [0,0,0,0,1,1,0,1,1]]
    
    for h in range(9):
        for i in range(9):
            matrix_row = i // 3  # Calculate the row index in the 'matrix' array
            matrix_col = i % 3   # Calculate the column index in the 'matrix' array

            # Use these indices to access the elements in 'matrix' and 'possible_presses'
            value += matrix[matrix_row][matrix_col] * possible_presses[h][i]
            value_modded = value % 3
            presses_needed[i] += value_modded
            #print(f"matrix[{matrix_row}][{matrix_col}] * pp[{h}][{i}] = {value}")

    for i in range(9):
        presses_needed[i] = presses_needed[i]%3
    #print(f"Value: {value}")
    #print(f"Value after mod: {value}")
    if value_modded == 0:
        return presses_needed
    else:
        return -1

#FUNCITONS******************************************************************************
        
def main():
    value_range = [0,1,2]
    number_of_solvable = 0
    number_of_presses_per_matrix = []
    #ask user to fill in initial state
    print("***The values coordinate to the following: 0=off, 1=red, 2=green***")

    input_matrix(matrices)
    
    print_matrices(matrices)

    for i in range(9):
        solvable_value = solvable(matrices[i])
        if(solvable_value != -1):
            number_of_presses_per_matrix.append(solvable_value)
            number_of_solvable += 1

    if number_of_solvable < 8:
        print("We cannot reach the 'all off state.'")
    else:
        print(f"Number of presses per box (array 1-9): {number_of_presses_per_matrix}")
        print("We can reach the 'all off state.'")

    #determine if can reach all off state
    #Function Here!!!!!!
        #If true, output number of pushes
        #Else, say it cannot be reached
    
main()
    