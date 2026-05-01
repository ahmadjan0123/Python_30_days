#practice on class 16
students = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 60},
    {"name": "Usman", "marks": 38},
    {"name": "Hina", "marks": 90}
]

print('task 1')

def task1(students):
    high1 = students[0]
    high_name1 = high1['name']
    high_marks1 = high1['marks']
    for i in students:
        if i['marks'] > 50:
            high_marks1 = i['marks']
            high_name1 = i['name']
    return high_name1

print(task1(students))

print('task 2')


def task2(students):
    failed_students = [ ]

    for i in students:
        if i['marks'] < 50:
            failed_students.append(i['name'])

    return failed_students

print(task2(students))

print('task 3')


def task3(students):

    status = {
        'failed' : 0,
        'passed' :0
    }

    for i in students:
        if i['marks'] >= 50:
            status["passed"] +=1
        else:
            status['failed'] +=1

    return status

print(task3(students))


print('task 4')

def task4(students):
    total = 0

    for i in students:
        if i['marks'] >=50:
            total += i['marks']

    return total

print(task4(students))



