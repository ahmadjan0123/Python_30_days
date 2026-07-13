class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    def showPerson(self):
        print(f'My name is {self.name} and age is {self.age}')


class Teacher(Person):
    def __init__(self, name, age,prof):
        super().__init__(name, age)
        self.prof = prof


    def showTeacher(self):
        self.showPerson()
        print(f'My profession is {self.prof}')



t1 = Teacher ('ahmad',19,'AI PROFESSOR')
t1.showTeacher()

# task for polymorphism

class Car:
    def __init__(self):
        pass
    def move(self):
        print('car is driving')


class Bike:
    def __init__(self):
        pass
        
    def move(self):
        print('the bike is riding')


class Airplan:
    def move(self):
        print('the plan is flying')


vehicles = [Car(),Bike(),Airplan()]

for x in vehicles:
    x.move()





#task - 2
class Lion:
    def __init__(self):
        pass
    def sound(self):
        print('lion:Roar')
class Dog:
    def sound(self):
        print('DOG: BARK')
class Cat:
    def sound(self):
        print('Cat: Meow')

class Cow:
    def __init__(self):
        pass
    def sound(self):
        print('Cow: Moo')

Animals = [Lion(),Dog(),Cat(),Cow()]

for animal in Animals:
    animal.sound()


#overriding

class Person:
    def __init__(self):
        pass
    def Introduce(self):
        print('I am a person')

class Student(Person):
    def  __init__(self):
        pass
    def Introduce(self):
        print('I am a student')


class Teacher(Person):
    def  __init__(self):
        pass
    def Introduce(self):
        print('I am a teacher')


p1 = Person()
s1 = Student()
t1 = Teacher()

p1.Introduce()
s1.Introduce()
t1.Introduce()


class Person1:
    def introduce(self):
        print('I am Person 1')

class Student1(Person1):

    def introduce(self):
        super().introduce()
        print('i am student')

s2 = Student1()
s2.introduce()

class Calculator:

    def multiply(self,*nums):
        total = 1
        for n in nums:
            total*=n

        return total
    

c1 = Calculator()
print(c1.multiply(2,3))
print(c1.multiply(1,3,5,6,7,7))
print(c1.multiply(45,67,89))


from abc import ABC , abstractmethod

class Animal:
    @abstractmethod
    def sound():
        pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius*3.14*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    


r = Rectangle(3,5)
c = Circle(5)

print(r.area())
print(c.area())
    
# multiple inheritance 


class Camera:
    def take_photo(self):
        print('I will click your photo')

class Phone:
    def call(self):
        print('I will make the call')

class SmartPhone(Camera,Phone):

    def __init__(self):
        super().__init__()

smart1 = SmartPhone()
smart1.take_photo()
smart1.call()