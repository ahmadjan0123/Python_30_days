#🧪 Session: Functions + Lists (Control + Aggregation Mastery)

students = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 60},
    {"name": "Usman", "marks": 38},
    {"name": "Hina", "marks": 90}
]

print('TASK 1')

def total_pass_marks(students):
    total = 0
    for i in students:
        if i['marks'] >= 50:
            total += i['marks']
    return total

print(total_pass_marks(students))

print('Task 2')

def count_failures(students):
    count = 0

    for i in students:
        if i['marks'] < 50:
            count+=1
    return count

print('task 3')

def top_student(students):
    high = students[0]
    high_marks = students[0]['marks']
    high_names = students[0]['name']
    for i in students:
        if i['marks'] > high_marks:
            high_marks = i['marks']
            high_names = i['name']

    return high_names

print(top_student(students))
