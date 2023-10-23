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
                            print("PLease input an integer between 0-2")
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
#FUNCITONS******************************************************************************
        
def main():
    value_range = [0,1,2]

    #ask user to fill in initial state
    input_matrix(matrices)
    
    print_matrices(matrices)
    #determine if can reach all off state
    #Function Here!!!!!!
        #If true, output number of pushes
        #Else, say it cannot be reached
    
main()
    