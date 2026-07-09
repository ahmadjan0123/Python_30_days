class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'Hello{self.name} your age is {self.age}')

s1 = Student('Ahmad',18)
print(s1.name)
print(s1.age)

s1.greet()

#task - 1
class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print('TITLE: ',self.title)
        print('AUTHOR: ',self.author)


b1 = Book('the 48 laws of power','forgot')
b1.display()

#task - 2
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print('Title:',self.name)
        print('Salary:',self.salary)


e1 = Employee('abdullah',45000)
e1.show_details()


#task - 3

class BankAccount:
    def __init__(self,account_holder,balance):
        self.name = account_holder
        self.balance = balance

    def show_balance(self):
        print(f'Name{self.name} \n Balance:{self.balance}')

b1 = BankAccount('Ahmad Yousuf Jan',70000)
b1.show_balance()
    

class Bank:

    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance -= amount

    def show(self):
        print(self.__balance)







b11 = Bank('ahmad',5000)
b11.deposit(100)
b11.withdraw(50)
b11.show()



# inheritance 


class Animal:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def show(self):
        print(f'Name:{self.name}\n Age:{self.age}')


class Dog(Animal):

    def __init__(self, name, age,food):
        super().__init__(name,age)
        self.food = food

    def show_food(self):
        print('FOOD:',self.food)

Dog1 = Dog('ahmad',19,'dog-food')
Dog1.show()
Dog1.show_food()

        
#task -1 // inheritance
class Vehicle:

    def __init__(self):
        pass
        

    def start_engine(self):
        print('parent function called')

class Car(Vehicle):

    def __init__(self):
        pass

    
c1 = Car()
c1.start_engine()

#task - 2
class Person:

    def __init__(self,name):

        self.name = name

    def introduce(self):
        print(f'i am {self.name}')


class Teacher(Person):

    def __init__(self, name,language):
        super().__init__(name)
        self.language = language

    def teach(self):
        self.introduce()
        print(f'I teach {self.language}')


t1 = Teacher('ahmad','java')
t1.teach()

# task - 3

class BankAccount1:

    def __init__(self,balance):
        self.__bal = balance

    def deposit(self,amount):
        self.__bal += amount

    def withdraw(self,amount):
        if (self.__bal >= amount):
            self.__bal -= amount
        else:
            print('insufficient funds')

    def show_bal(self):
        print(self.__bal)

b12 = BankAccount1(100)
b12.deposit(500)
b12.withdraw(300)
b12.show_bal()

