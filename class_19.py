#🧪 CLASS 19 — Dictionaries + Lists (Real Data Simulation)

data = [
    {"name": "Ali", "marks": [70, 80, 90]},
    {"name": "Ahmed", "marks": [40, 50, 45]},
    {"name": "Sara", "marks": [88, 92, 85]}
]


def student_averages(data):
    new_list = []
    for i in data:
        total = 0
        for m in i['marks']:
            total += m
        avg = total/len(i['marks'])
        new_list.append({

            'name': i['name'],
            'avg': avg
        })
    return new_list

print(student_averages(data))


print('This is task 2')

def class_topper(data):

    new_list1 = []

    for x in data:
        tot = 0

        for f in x['marks']:
            tot += f
        avg1 = tot / len(x['marks'])
        new_list1.append({
            'name' : x['name'],
            'avg' : avg1
        })

    high = new_list1[0]
    name = high['name']
    for s in new_list1:
        if s['avg'] > high['avg']:
            high = s['avg']
            name = s['name']
    return name


print(class_topper(data))

print('task 3')    

def failed_students(data):
    new_list2 = []

    for u in data:
        tot1 = 0
        for t in u['marks']:
            tot1 += t
        avg2 = tot1/len(u['marks'])
        new_list2.append({
            'name' : u['name'],
            'avg':avg2
    })

    low = new_list2[0]
    name1 = None
    
    failed_students = []
    for o in new_list2:
        if o['avg'] < 50:
            name1 = o['name']
            failed_students.append(name1)


    return failed_students

print(failed_students(data))

