'''
Linear Games -- Game 2 Part 1

Write a program that starts with a random configuration and then allows the user to change the state
of each button (i.e. pushing each switch). Your function should state the initial configuration and then
each configuration after a switch is pushed.
'''

import random

bulb = []

# 0="off", 1="red", 2="green"
for i in range(3):
    bulb.append(random.randint(0,2))
    
print("Initial state: ", bulb)

done = False
while not done:
    user_input = input("Which switch would you like to hit?")
    if user_input == 'A':
        if bulb[0] < 2:
            bulb[0] = bulb[0] + 1
            if bulb[1] < 2:
                bulb[1] = bulb[1]+1
            elif bulb[1] == 2:
                bulb[1] = 0
        elif bulb[0] == 2:
            bulb[0] = 0
            if bulb[1] < 2:
                bulb[1] = bulb[1]+1
            elif bulb[1] == 2:
                bulb[1] = 0
        print("New state: ", bulb)
        
    if user_input == 'B':
        if bulb[1] < 2:
            bulb[1] = bulb[1]+1    
        elif bulb[1] == 2:
            bulb[1] = 0
        
        if bulb[2] < 2:
            bulb[2] = bulb[2]+1
        elif bulb[2] == 2:
            bulb[2] = 0
        
        if bulb[0] < 2:
            bulb[0] = bulb[0]+1
        elif bulb[0] == 2:
            bulb[0] = 0
        
        print("New state: ", bulb)
        
    if user_input == 'C':
        if bulb[2] < 2:
            bulb[2] = bulb[2]+1 
        elif bulb[2] == 2:
            bulb[2] = 0
            
        if bulb[1] < 2:
            bulb[1] = bulb[1]+1
        elif bulb[1] == 2:
            bulb[1] = 0
        print("New state: ", bulb)

    check = input("Would you like to go again?")
    if check == 'yes':
        done = False
    if check == "no":
        done = True