#FUNCTION

# this is a simple function with no parameter 
'''
def greet():
    print("HELLO")


greet()
'''

# THIS IS A CONSTRUCTOR WITH A PARAMETER
'''
def greet(name):
    print(f"Hello {name}")

greet('Ahmad')
greet("HAMZA")

'''
'''
def add(a,b):
    print(a+b)

add(10,5)
 '''
'''
def even_check(num):
    if (num%2==0):
        print("even")
    else:
        print("Odd")


even_check(5)
even_check(10)
'''
'''
def print_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

print_table(5)
print_table(10)
'''

# function with a return value

def sqaure(a):
    return a*a


result = sqaure(5)
print(result)

def is_even(num):
    if (num%2==0):
        return True
    else:
        return False
task_2 = is_even(6)
print(task_2)

def max_of_two(c,d):
    if (c>d):
        return c
    else:
        return d
    
task_3 = max_of_two(12,5)
print(task_3)


def calculate(a,b,opp):
    if (opp == "+"):
        return a+b
    elif (opp == "-"):
        return a-b
    elif (opp == "*"):
        return a*b
    elif (opp=="/"):
        return a/b
    else:
        return "Invalid Operand"

task_4_add = calculate(10,10,"@")
print(task_4_add)




