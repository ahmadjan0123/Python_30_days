#Session: Functions + Lists (Problem Solving Core)
students = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 58}
]


#task1 have been achieved through list comprehion. which makes it better and efficient
TASK1  = [s['name'].upper()  for s in students if s['marks']>60]
print(TASK1)


print("TASK 2")
print(len(students))

#task 2 through compresion
avg = sum(s['marks'] for s in students) / len(students)

def average_marks(students):
    avg = 0
    total = 0
    for s in students:
        total += s['marks']

    avg = total/len(students)
    return avg

print(average_marks(students))


print('TASK 3')

def highest_marks(students):
    high = list(students)[0]
    high_marks = high['marks']

    for i in students:
        if i['marks'] > high_marks:
            high = i

        return i
    

print(highest_marks(students))



print('TASK 4')

def count(students):
    counter = 0
    for i in students:
        if i['marks'] >= 50:
            counter +=1

    return counter

print(count(students))

print('TASK 5')


def spicy_task(students):
    new = {
        'pass':  [], 
        'fail': []
    }
    for s in students:
        if s['marks'] > 50:
            new['pass'].append(s['name'])
        else:
            new['fail'].append(s['name'])

    return new

print(spicy_task(students))