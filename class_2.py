# day 2
# understand conditional operator

#TASK 1
'''
age = int(input("Enter user age: "))

if age>= 18:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
'''
''''
#TASK 2

marks = int(input("ENTER YOUR MARKS: "))

if marks>=90:
    print("A+ Grade")
elif marks >=80:
    print("A Grade")
elif marks>=70:
    print("B+ Grade")
elif marks>=60:
    print("C Grage")
else:
    print("FAIL")
    '''

#TASK 3

#PRACTICE PROBLEM
'''
age = int(input("Enter your age: "))
has_idcard = input("Enter 1 if you have and 0 if you dont have: ")
has_id = (has_idcard == "1") # comparisson

print(has_id)


if age >= 18 and has_id:
    print("acess granted")
elif age < 18 and has_id:
    print("Underage but access granted")
else:
    print("ACCESS DENIED")

'''

#TASK 4
#STYLE
'''
age = int(input("Enter your age: "))

if age < 0 or age > 120: # validation
    print("Invalid Age")
elif age < 18:
    discount = 10
    print(f"Your Discount is {discount}%")
elif age >= 65:
    discount = 20
    print(f"Your Discount is {discount}%")
else:
    discount = 5
    print(f"Your discount is {discount}%")
    '''
#TASK 5
#CLEANER VERSION
age = int(input("Enter your age: "))

if age < 0 or age > 120: # validation
    print("Invalid Age")
else:
    if (age < 18):
        discount = 10
    elif (age >=65):
        discount = 20
    else:
        discount = 5

    print(f"Your discount is {discount}%")