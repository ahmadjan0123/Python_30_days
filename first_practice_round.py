# code snipet 1
'''
Write a Python program:

Requirements:
Take a list of numbers
Find the maximum number
Print it

'''

list1 = [2,5,6,8,9]
m = list1[0]

for i in list1:
    if i>m:
        m = i

print(m)


''''should only print even numbers'''
list2 = [1, 2, 3, 4, 5]
for r in list2:
    if (r%2==0):
        print(r)


''' write the names and marks 2.write the topper name'''
students = {
    "Ali": 78,
    "Sara": 92,
    "Ahmed": 85,
    "Zain": 88
}

for q in students:
    print(q,students[q])


# task 2
topper_name = list(students.keys())[0]
topper_marks = list(students.values())[0]


for t in students:
    if students[t]>topper_marks:
        topper_marks = students[t]
        topper_name = t
print(topper_name,topper_marks)


'''

1. View all students
2. Add student
3. Find topper
4. Search student
5. Exit

print('')


students1 = {
    "Ali": 
    {"marks": 78, "age": 18
    },
    "Sara": 
    {"marks": 92, "age": 19
    },
    "Ahmed": {"marks": 85, "age": 18
    },
    "Zain": {"marks": 88, "age": 20}
}

#1
for u in students1:
    print(u,students1[u]['age'],students1[u]['marks'])

#2 
students1["Hamza"] = {"marks":98,"age":56}

#task 3- find topper

to = students1['Ali']['marks']
to_name  = list(students1.keys())[0]
print(to)

for a in students1:
    if students1[a]['marks'] > to:
        to =  students1[a]['marks'] 
        to_name = a

print(to,to_name)



target = input("Enter the name you want to search")
state = True
while state:
    if target in students1:
        print(f"Name found")
        state = False
    else:
        print(f"Name not found")
        break
'''

st3 = {
    "Ali": {"marks": 78, "age": 18},
    "Sara": {"marks": 92, "age": 19},
    "Ahmed": {"marks": 85, "age": 18},
    "Zain": {"marks": 88, "age": 20}
}

state = True
while state:
    print("1 for updating")
    print("2 for deleting")
    print("3 for viewing")
    print("4 for searching")
    print("5 to exit")
    choice = input("Enter your choice")
    if choice == "1":
        print("You have choosen 1-to update")
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        score=  int(input("Enter the marks: "))
        st3[name] = {"marks": score,"age":age}
    elif choice == "2":
        print("You choose 2-deletion")
        name = input("Enter the name: ")
        if name in st3:
            del st3[name]
            print("Deleted Successfully")
    elif choice == "3":
        print("you choose 3-to view")
        for i in st3:
            print(i,st3[i]['marks'],st3[i]['age'])
    elif choice == "4":
        print("You have choose to search")
        name = input("Enter the name: ")
        if name in st3:
            print(f"Name: {name},Marks: {st3[name]['marks']},Age: {st3[name]['age']}")
        else:
            print(f"{name} not found")
    elif choice == "5":
        print("you choose to end")
        state = False
    else:
        print("Invalid operation entered")