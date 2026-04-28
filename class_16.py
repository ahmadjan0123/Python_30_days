# working on mistakes

students = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 60}
]

#task 1

def task1(students):

    total = 0
    for i in students:
         if i['marks'] >= 50:
            total += i['marks']
    
    return total


print(task1(students))


print('task 2')

def task2(students):
    counter = 0

    for i in students:
        if i['marks'] < 50:
            counter += 1
    return counter

print(task2(students))


print('task 3')

def task3(students):

    high_name = students[0]['name']
    high_marks = students[0]['marks']
    for i in students:
        if i['marks'] > high_marks:
            high_marks = i['marks']
            high_name = i['name']

    return high_name



print(task3(students))

print('task 4')

def task4(students):
    passed = task1(students)

    avg = passed/3
    return avg

print(task4(students))



#INTERMEDIATE TASKS

print('task 1.1')

def convert_marks(students):

    result = []

    for i in students:
        if i['marks'] >=80:
            grade = 'A'
        elif i['marks'] >= 50:
            grade = 'B'
        else:
            grade = 'C'
        
        result.append({

        "name": i['name'],
        "grade" : grade}
    )
    return result

print('task 1.3')

def counterr(students):

    count = {
        "A" : 0,
        "B" : 0,
        "C" : 0
    }

    for i in students:
        if i['marks'] >= 80:
            count['A'] += 1
        elif i['marks'] >= 50:
            count['B'] += 1
        else:
            count["C"] +=1

    return count

print('task 1.4')

def topper(students):
    high_marks = -1
    high_name = None

    for i in students:
        if i['marks'] >= 50:
            if i['marks'] >high_marks:
                high_marks = i ['marks']
                high_name = i['name']

    return high_name

print(topper(students))
    



            

    
