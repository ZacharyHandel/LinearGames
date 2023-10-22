#This is the main file for Linear Games 3
import random

#Create matrices variable that contains all if the matrices we want to work upon
matrices = [
]

#FUNCITONS******************************************************************************
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
    print(matrices[int(matrix)])
#FUNCITONS******************************************************************************

win = False
h=0
i=0
j=0
value_range = [0,1,2]

#Fill matrices randomly
# Fill each matrix with random values
for i in range(9):
    matrix = [[random.randint(0, 2) for _ in range(3)] for _ in range(3)]
    matrices.append(matrix)

#UNTIL WIN
while not win:
    #print matrices
    print_matrices(matrices)
    #Store selected matrix in temp variable
    selected_matrix = input("Which matrix would you like to alter?: ")

    print_matrix(int(selected_matrix)-1)
    #Ask use for which element in that matrix they want to edit
    #Store selected element in temp variable
    selected_element = input("Which value would you like to press?: ")
    
    #CALL ALTER FUNCTION
    
    #SHOW Altered Matrix
    
    #Loop through all matrices
        #If all elements are 0
            #Win!
        #Else
            #No win yet
    
    
    
    