'''
Linear Games -- Game 2 Part 2

Write a program that takes an initial configuration from the user and determines if after a series of
switches are “pushed” all lights will be in the off state. The output should be either ”We cannot reach
the “all off” state” or gives the number of times each switch must be pressed to achieve the “all off
state”.
'''

def isTwo(light, pos):
    if light[pos] == 2:
        return True
    else:
        return False
    
    

def main():
    bulb = []

    for i in range(3):
        bulb.append(int(input("Enter a value from 0-2 for the configuration of the bulbs: ")))

    print("Initial Configuration: ", bulb)

    count = 0
    if bulb == [0,0,0]:
        print("The bulbs are all off")

    elif bulb == [1,0,0]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,1,0]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,0,1]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,1,0]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,1,1]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,1,1]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,0,1]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,0,0]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,1,0]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,2,0]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,2,0]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,2,1]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,2,2]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,2,1]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,2,2]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,1,2]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,2,0]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,0,2]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,0,2]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2,1,2]:
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0,1,2]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [1,0,2]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")    

    elif bulb == [0, 2, 1]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [0, 2, 2]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2, 0, 1]:
        print("Switch A")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")

    elif bulb == [2, 1, 1]:
        print("Switch C")
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print("Switch B")
        bulb[0] = (bulb[0] + 1) % 3
        bulb[1] = (bulb[1] + 1) % 3
        bulb[2] = (bulb[2] + 1) % 3
        count += 1
        print("New State: ", bulb)
        print(f"The all off state was reached in {count} steps")
        
main()