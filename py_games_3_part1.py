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
    for row in matrices[matrix]:
        print(' '.join(map(str, row)))
#FUNCITONS******************************************************************************

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
        
def alter_matrix(matrix_num, element_num):
    #print (matrices[matrix_num])
    #print (matrices[matrix_num][0][element_num])
    #print(matrices[matrix_num][1][0])
    if element_num >= 0 and element_num <=2:
        #row1
        #print("row 1")
        
        #element 1 is pressed
        if element_num == 0:
            num = matrices[matrix_num][0][element_num] + 1
            num2 = matrices[matrix_num][0][1] + 1
            num3 = matrices[matrix_num][1][0] + 1
            num4 = matrices[matrix_num][1][1] + 1
            
            if num > 2:
                matrices[matrix_num][0][element_num] = 0
            else:
                matrices[matrix_num][0][element_num] += 1
            if num2 > 2:
                matrices[matrix_num][0][1] = 0
            else:
                matrices[matrix_num][0][1] += 1
            if num3 > 2:
                matrices[matrix_num][1][0] = 0
            else:
                matrices[matrix_num][1][0] += 1
            if num4 > 2:
                matrices[matrix_num][1][1] = 0
            else:
                matrices[matrix_num][1][1] += 1
        #element 2 is pressed
        if element_num == 1:
            num = matrices[matrix_num][0][element_num] + 1
            num2 = matrices[matrix_num][0][0] + 1
            num3 = matrices[matrix_num][0][2] + 1
            
            
            if num > 2:
                matrices[matrix_num][0][element_num] = 0
            else:
                matrices[matrix_num][0][element_num] += 1
            if num2 > 2:
                matrices[matrix_num][0][0] = 0
            else:
                matrices[matrix_num][0][0] += 1
            if num3 > 2:
                matrices[matrix_num][0][2] = 0
            else:
                matrices[matrix_num][0][2] += 1
        #element 3 is pressed
        if element_num == 2:
            num = matrices[matrix_num][0][element_num] + 1
            num2 = matrices[matrix_num][0][1] + 1
            num3 = matrices[matrix_num][1][1] + 1
            num4 = matrices[matrix_num][1][2] + 1
            
            if num > 2:
                matrices[matrix_num][0][element_num] = 0
            else:
                matrices[matrix_num][0][element_num] += 1
            if num2 > 2:
                matrices[matrix_num][0][1] = 0
            else:
                matrices[matrix_num][0][1] += 1
            if num3 > 2:
                matrices[matrix_num][1][1] = 0
            else:
                matrices[matrix_num][1][1] += 1
            if num4 > 2:
                matrices[matrix_num][1][2] = 0
            else:
                matrices[matrix_num][1][2] += 1
    elif element_num >= 3 and element_num <=5: 
        #row2
        #print("row 2")
        #element 4 is pressed
        if element_num == 3:
            num = matrices[matrix_num][1][0] + 1
            num2 = matrices[matrix_num][0][0] + 1
            num3 = matrices[matrix_num][2][0] + 1
            
            
            if num > 2:
                matrices[matrix_num][1][0] = 0
            else:
                matrices[matrix_num][1][0] += 1
            if num2 > 2:
                matrices[matrix_num][0][0] = 0
            else:
                matrices[matrix_num][0][0] += 1
            if num3 > 2:
                matrices[matrix_num][2][0] = 0
            else:
                matrices[matrix_num][2][0] += 1
            
        #element 5 is pressed
        if element_num == 4:
            num = matrices[matrix_num][1][1] + 1
            num2 = matrices[matrix_num][0][1] + 1
            num3 = matrices[matrix_num][1][0] + 1
            num4 = matrices[matrix_num][1][2] + 1
            num5 = matrices[matrix_num][2][1] + 1
            
            
            if num > 2:
                matrices[matrix_num][1][1] = 0
            else:
                matrices[matrix_num][1][1] += 1
            if num2 > 2:
                matrices[matrix_num][0][1] = 0
            else:
                matrices[matrix_num][0][1] += 1
            if num3 > 2:
                matrices[matrix_num][1][0] = 0
            else:
                matrices[matrix_num][1][0] += 1
            if num4 > 2:
                matrices[matrix_num][1][2] = 0
            else:
                matrices[matrix_num][1][2] += 1
            if num5 > 2:
                matrices[matrix_num][2][1] = 0
            else:
                matrices[matrix_num][2][1] += 1
        #element 6 is pressed
        if element_num == 5:
            num = matrices[matrix_num][1][2] + 1
            num2 = matrices[matrix_num][0][2] + 1
            num3 = matrices[matrix_num][2][2] + 1
            
            if num > 2:
                matrices[matrix_num][1][2] = 0
            else:
                matrices[matrix_num][1][2] += 1
            if num2 > 2:
                matrices[matrix_num][0][2] = 0
            else:
                matrices[matrix_num][0][2] += 1
            if num3 > 2:
                matrices[matrix_num][2][2] = 0
            else:
                matrices[matrix_num][2][2] += 1
    else:
        print("row 3")
        #row3
        #element 7 is pressed
        if element_num == 6:
            num = matrices[matrix_num][2][0] + 1
            num2 = matrices[matrix_num][1][0] + 1
            num3 = matrices[matrix_num][1][1] + 1
            num4 = matrices[matrix_num][2][1] + 1
            
            
            if num > 2:
                matrices[matrix_num][2][0] = 0
            else:
                matrices[matrix_num][2][0] += 1
            if num2 > 2:
                matrices[matrix_num][1][0] = 0
            else:
                matrices[matrix_num][1][0] += 1
            if num3 > 2:
                matrices[matrix_num][1][1] = 0
            else:
                matrices[matrix_num][1][1] += 1
            if num4 > 2:
                matrices[matrix_num][2][1] = 0
            else:
                matrices[matrix_num][2][1] += 1
            
        #element 8 is pressed
        if element_num == 7:
            num = matrices[matrix_num][2][1] + 1
            num2 = matrices[matrix_num][2][0] + 1
            num3 = matrices[matrix_num][2][2] + 1
            
            if num > 2:
                matrices[matrix_num][2][1] = 0
            else:
                matrices[matrix_num][2][1] += 1
            if num2 > 2:
                matrices[matrix_num][2][0] = 0
            else:
                matrices[matrix_num][2][0] += 1
            if num3 > 2:
                matrices[matrix_num][2][2] = 0
            else:
                matrices[matrix_num][2][2] += 1
            
        #element 9 is pressed
        if element_num == 8:
            num = matrices[matrix_num][2][2] + 1
            num2 = matrices[matrix_num][2][1] + 1
            num3 = matrices[matrix_num][1][1] + 1
            num4 = matrices[matrix_num][1][2] + 1
            
            if num > 2:
                matrices[matrix_num][2][2] = 0
            else:
                matrices[matrix_num][2][2] += 1
            if num2 > 2:
                matrices[matrix_num][2][1] = 0
            else:
                matrices[matrix_num][2][1] += 1
            if num3 > 2:
                matrices[matrix_num][1][1] = 0
            else:
                matrices[matrix_num][1][1] += 1
            if num4 > 2:
                matrices[matrix_num][1][2] = 0
            else:
                matrices[matrix_num][1][2] += 1

def main():
    win = False
    h=0
    i=0
    j=0
    value_range = [0,1,2]

    fill_random(matrices)
    #fill_zeros(matrices)

    #UNTIL WIN
    while not win:
        #print matrices
        print_matrices(matrices)
        #Store selected matrix in temp variable
        try:
            selected_matrix = int(input("Which matrix would you like to alter?: "))
            if 1 <= selected_matrix <=9:
                print_matrix(int(selected_matrix)-1)
                try:
                    selected_element = int(input("Which value would you like to press?: "))
                    if 1 <= selected_element <=9:
                        alter_matrix(int(selected_matrix)-1, int(selected_element)-1)
                    else:
                        print("Please input an integer between 1-9")
                except ValueError:
                    print("Please input an integer between 1-9")
            else:
                print("Please input an integer between 1-9")
        except ValueError:
            print("Please input an integer between 1-9")
        #Ask use for which element in that matrix they want to edit
        #Store selected element in temp variable
    
        #print(check_win(matrices))
        #CALL ALTER FUNCTION
    
        #SHOW Altered Matrix
    
        #Loop through all matrices
            #If all elements are 0
                #Win!
            #Else
                #No win yet
        if check_win(matrices) == True:
            print("Win!")
            return win
        else:
            print("No win yet")
    
main()
    
