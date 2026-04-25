#List Comprehension (Python’s Cheat Code)
lst = [1,2,3,4]
result = [i*2 for i in lst]
print(result)



#FILTERING
filtering = [i for i in lst if i%2==0]
print(filtering)

#combining
combining = [i*2 for i in lst if i%2==0]
print(combining)

print("TASK 1")
task1 = [1,2,3,4]

res = [i+5 for i in task1]
print(res)

print("TASK 2")

task2 = [1,2,3,4,5]
result2 = [ i for i in task2 if i%2!=0]
print(result2)

print("TASK 3")
task3= [1,3,10,14]
result3 = [i*i for i in task3 if i>10]
print(result3)


#NEW TOPIC: Nested List Comprehension

#traditional way 
list1 = [ [1,2,3],[4,5],[6,7,8]]
print(list1[1])
nest = []
for subset in list1:
    for item in subset:
        nest.append(item)

print(nest)

#through compression

practice1 = [item for sublist in list1 for item in sublist]
print(practice1)


practice2 = [item for sublist in list1 for item in sublist if item%2==0]
print(practice2)

practice3 = [item**2 for sublist in list1 for item in sublist]
print(practice3)


print("task 1")

task1 = [[2,4], [6,8], [10]]

ans1 = [item for subitem in task1 for item in subitem]
print(ans1)


print("TASK 2")


ans2 = [item for subitem in task1 for item in subitem if item>5]
print(ans2)


print("TASK 3")

ans3 = [item**2 for subitem in task1 for item in subitem if item%2==0]
print(ans3)



#Dictionaries + List Comprehension

students = [
    {"name": "Ali", "marks": 80},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 90}
]


pr1 = [s['name'] for s in students if s['marks']>50]
print(pr1)

marks = [s['marks'] for s in students]
print(marks)


increment_5 = [s['marks']+5 for s in students]
print(increment_5)

low = [s['name'] for s in students if s['marks']<60]
print(low)


print("TASKS OF LIST COMPREHENSION")
print("TASK 1")

students1 = [
    {"name": "Ali", "marks": 80},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 90},
    {"name": "Zain", "marks": 30}
]

t1 = [s['name'] for s in students1 if s['marks']>70]
print(t1)

print("TASK 2")

t2 = [s['name'] for s in students1 if s['marks']<50]
print(t2)


print("TASK 3")

t3 = ["PASS" if s["marks"]>50 else "FAIL" for s in students1]
print(t3)