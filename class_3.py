#class 3
#LOOPS 


#WHILE LOOPS
'''
counter = 1

while counter <= 10:
    print(counter)
    counter +=1
    '''

# WHILE LOOPS WITH USER CONTROLLED END
'''
running = True

while running:

    number = input("Enter stop to exit: ")

    if ( number == "stop"):
        running = False 
'''
#WHILE LOOP CHALLENGE
'''
running = True

while running:
    number = input("ENTER THE NUMBER(STOP TO EXIT: )")
    if(number == "stop"):
        running = False
    else:
        print(f"NUMBER: {number}")
'''
#calculator with while loop

'''

while True:

    print("Choose from the menu: ")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for division")
    print("4 for multiplication")
    print("5 to end")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is {num1+num2}")
    elif choice == "2":
        print("You choose subtraction")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter second number: "))
        print(f"The subtraction of {num1} and {num2} is {num1-num2}")
    elif choice == "3":
        print("You choose division")
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter second number: "))
        print(f"The divison of {num1} and {num2} is {num1/num2}")
    elif choice == "4":
        print("You choose multiplication")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter second number: "))
        print(f"The product of {num1} and {num2} is {num1*num2}")
    elif choice == "5":
        print("PROGRAM ENDED")
        break
    else:
        print("INVALID CHOICE")
'''

#for loop
'''
for i in range(1,6):
    print(i)
    '''
'''
#task 1
for i in range(1,11):
    print(f"Number: {i}")
    '''
'''
#task 2
for i in range(2,21,2):
    print(f"Number:  {i}")
    '''
'''
#task 3
number = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{number} * {i} = {number*i}")



'''
running = True

while running:
    num = int(input("Enter the number: "))
    if (num == 0):
        break

