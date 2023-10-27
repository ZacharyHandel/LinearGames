import random
labels = ['A','B','C','D','E']
user_l = []
for letter in labels:
    user_in = random.randint(0,1)
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
ans = 'Y'
print("\n")
while ans != 'n' and ans != 'N':
    print("Change which bulb (A, B, C, D or E)?")
    choice = input()
    if choice == 'A':
        change(user_l, 0)
    elif choice == 'B':
        change(user_l, 1)
    elif choice == 'C':
        change(user_l, 2)
    elif choice == 'D':
        change(user_l, 3)
    elif choice == 'E':
        change(user_l, 4)
    else:
        print("Invalid input")
        break
    for i in range(5):
        print(user_l[i], end=" ")
    print()
    print("Change another bulb? (Y or N)")
    ans = input()
    print(ans)
    
    

