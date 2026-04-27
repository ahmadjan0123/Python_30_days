#Aggregation + Control Flow Mastery (Functions + Lists)
students = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 60}
]


print('task 1')
def get_total_marks(students):
    total = 0

    for i in students:
        total += i['marks']

    return total


print(get_total_marks(students))

print('task 2')


def get_average_marks(students):
   
   total = get_total_marks(students) # we have declared total function twice so now we doen need to recalculate we simply call it through the other function. this will save us time as well as space and improve code reuseability
   avg = total/len(students)
   return avg
   ''' total = 0
    for i in students:
        total += i['marks']
    avg = total/len(students)
    return avg
'''
print(get_average_marks(students))


print('task 3')

def count_pass(students):
    counter  = 0

    for i in students:
        if i['marks'] >= 50:
            counter += 1
    return counter

print(count_pass(students))


print('task 4')

def get_top_students(students):
    li = []
    for i in students:
        if i['marks'] > 70:
            li.append(i['name'])

    return li

print(get_top_students(students))



#Filtering + Transformation + Aggregation (Combined Thinking)
students1 = [
    {"name": "Ali", "marks": 75},
    {"name": "Ahmed", "marks": 45},
    {"name": "Sara", "marks": 82},
    {"name": "Zara", "marks": 60}
]

print('task 1.1')

def total_pass_marks1(students):
    tot = 0

    for i in students:
        if i['marks'] >= 50:
            tot+= i['marks']

    return tot

print(total_pass_marks1(students))


print('Task 1.2')

def avg_top_students1(students):
    counterr = 0
    total_avg = 0
    for i in students:
        if i['marks'] > 70:
            total_avg += i['marks']
            counterr += 1
    avg_condition_based = total_avg/counterr

    return avg_condition_based

print(avg_top_students1(students))


print('task 1.3')

def count_A_students(students1):

    name_count = 0
    for  i in students1:
        if i['name'].startswith('A'):
            name_count+=1

    return name_count

print(count_A_students(students1))

print('task 4')

def add_bonus(students):

    updated_marks = []

    for i in students1:
        new_students = {
            "name" : i['name'],
            "mark" : i['marks']+5
        }
        updated_marks.append(new_students)
    return updated_marks

print(add_bonus(students1))