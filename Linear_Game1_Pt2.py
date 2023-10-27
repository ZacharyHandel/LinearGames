import random
labels = ['A','B','C','D','E']
user_l = []
print("Enter the state of label 1 - on, 0 - off")
for letter in labels:
    print("Label", letter,":", end=" ")
    user_in = int(input())
    user_l.append(user_in)
for i in range(5):
    print(user_l[i], end=" ")
   
def change_adj(num):
    if user_l[num] == 0:
        user_l[num] = 1
        #print(light_bulbs[num])
    else:
        user_l[num] = 0
   
def change(bulbs, number):
    if bulbs[number] == 0:
        bulbs[number] = 1
        print()
        #print(light_bulbs[number])
        if number == 0:
            change_adj(number+1)
        elif number == 4:
            change_adj(number-1)
        else:
            change_adj(number+1)
            change_adj(number-1)
    else:
        bulbs[number] = 0
        print()
        #print(light_bulbs[number])
        if number == 0:
            change_adj(number+1)
        elif number == 4:
            change_adj(number-1)
        else:
            change_adj(number+1)
            change_adj(number-1)
presses = [0,0,0,0,0]
optimal = [0, 0, 0, 0, 0]
case1 = [1, 1, 0, 0, 0,]
case2 = [0, 0, 0, 1, 1,]
case3 = [0, 1, 1, 1, 0]
case4 = [1, 1, 1, 0, 0,]
case5 = [0, 0, 1, 1, 1]
case6 = [1, 1, 0, 1, 1]
case7 = [1, 0, 1, 0, 0]
case8 = [1, 0, 0, 1, 0]
case9 = [1, 0, 0, 0, 1]
case10 = [0, 1, 1, 0, 0]
case11 = [0, 1, 0, 1, 0]
case12 = [0, 1, 0, 0, 1]
case13 = [0, 0, 1, 1, 0]
case14 = [0, 0, 1, 0, 1]
case15 = [1, 1, 0, 1, 0]
case16 = [1, 1, 0, 0, 1]
case17 = [1, 0, 1, 1, 0]
case18 = [1, 0, 1, 0, 1]
case19 = [1, 0, 0, 1, 1]
case20 = [0, 1, 1, 0, 1]
case21 = [0, 1, 0, 1, 1]
case22 = [1, 1, 1, 1, 0]
case21 = [1, 1, 1, 0, 1]
case22 = [1, 0, 1, 1, 1]
case23 = [0, 1, 1, 1, 1]
case24 = [1, 1, 1, 1, 1]
case25 = [0, 0, 0, 0, 0]
list_of_cases = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10,
    case11, case12, case13, case14, case15, case16, case17, case18, case19, case20, case21,
        case22, case23, case24, case25]
'''
for i in list_of_cases:
    print(i)
'''
count = 0
while user_l != optimal:
    if user_l[0] != optimal[0] or user_l[1] != optimal[1] or user_l[2] != optimal[2] or user_l[3] != optimal[3] or user_l[4] != optimal[4]:
        if user_l == case1:
            change(user_l, 0)
            presses[0] += 1
            count += 1
        elif user_l == case2:
            change(user_l, 4)
            presses[4] += 1
            count += 1
        elif user_l == case3:
            change(user_l, 2)
            presses[2] += 1
            count += 1
        elif user_l == case4:
            change(user_l, 1)
            presses[1] += 1
            count += 1
        elif user_l == case5:
            change(user_l, 3)
            presses[3] += 1
            count += 1
        elif user_l == case6:
            change(user_l, 0)
            change(user_l, 4)
            presses[0] += 1
            presses[4] += 1
            count += 2
        elif user_l == case7:
            print("We cannot reach the all off state")
            break
        elif user_l == case8:
            change(user_l, 3)
            change(user_l, 4)
            change(user_l, 0)
            change(user_l, 2)
            presses[3] += 1
            presses[4] += 1
            presses[0] += 1
            presses[2] += 1
            count += 4
            
        elif user_l == case9:
            change(user_l, 2)
            change(user_l, 3)
            change(user_l, 0)
            presses[2] += 1
            presses[3] += 1
            presses[0] += 1
            count += 3
        elif user_l == case10:
            print("We cannot reach the all off state")
            break
        elif user_l == case11:
            change(user_l, 1)
            change(user_l, 2)
            change(user_l, 0)
            presses[1] += 1
            presses[2] += 1
            presses[0] += 1
            count += 3
        elif user_l == case12:
            change(user_l, 4)
            change(user_l, 1)
            change(user_l, 2)
            change(user_l, 0)
            presses[4] += 1
            presses[1] += 1
            presses[2] += 1
            presses[0] += 1
            count += 4
        elif user_l == case13:
            print("We cannot reach the all off state")
            break
        
        elif user_l == case14:
            print("We cannot reach the all off state")
            break
        elif user_l == case15:
            print("We cannot reach the all off state")
            break
        elif user_l == case16:
            print("We cannot reach the all off state")
            break
        elif user_l == case17:
            change(user_l, 2)
            change(user_l, 0)
            presses[2] += 1
            presses[0] += 1
            count += 2
        elif user_l == case18:
            change(user_l, 4)
            change(user_l, 0)
            change(user_l, 2)
            presses[4] += 1
            presses[0] += 1
            presses[2] += 1
            count += 3
        elif user_l == case19:
            print("We cannot reach the all off state")
            break
        elif user_l == case20:
            change(user_l, 3)
            change(user_l, 1)
            change(user_l, 2)
            change(user_l, 0)
            presses[3] += 1
            presses[1] += 1
            presses[2] += 1
            presses[0] += 1
            count += 4
        elif user_l == case21:
            print("We cannot reach the all off state")
            break
        elif user_l == case22:
            print("We cannot reach the all off state")
            break
        elif user_l == case23:
            print("We cannot reach the all off state")
            break
        elif user_l == case24:
            change(user_l, 4)
            change(user_l, 1)
            presses[4] += 1
            presses[1] += 1
            count += 2
        else:
            presses[0] = 0
       
        print(user_l)
        #print("no")
print("optimal solution took", count, "iterations")
ct = 0
for i in labels:
    print("Presses for bulb:",i,presses[ct])
    ct += 1
