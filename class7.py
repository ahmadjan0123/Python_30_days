students = [

    {'name':'ahmad','age':67},
    {'name':'baryal','age':20},
    {'name':'hamza','age':21}


]

print(students[0]['age'])

for n in students:
    print(n['name'],n['age'])


#Task 1
students1 = [
    {"name": "Ahmad", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ali", "marks": 78}
]

print(students1[1]['marks'])
print(students1[2]['name'])
#task 2
for q in students1:
    #print(q['name'], "got", q['marks'])
    print(f"{q['name']} got {q['marks']}")

#task 3
total = 0
for t in students1:
    total += t['marks']
print(total)

#task 4
num = len(students1)
avg = total/num
print(avg)

#task 5
h1 = students1[0]['marks']
name = students1[0]['name']

for a in students1:
    if a['marks'] > h1:
        h1 = a['marks']
        name = a['name']

print(f"Topper is {name} with {h1} marks")

#task 6
students1.append({"name": "Usman", "marks": 88})

for u in students1:
    print(f"{u['name']},{u['marks']}")