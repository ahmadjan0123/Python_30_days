#🔥 Python Class 20 — Control + Aggregation Mastery

data = [
 {'name': 'Ali', 'marks': [80, 90, 85]},
 {'name': 'Sara', 'marks': [40, 50, 45]},
 {'name': 'John', 'marks': [70, 75, 80]}
]

# TASK-1: Filter + Aggregate

def high_scorers(data):
    new_list = []

    for u in data:
       total = 0
       for i in u['marks']:
           total += i
       avg = total/len(u['marks'])
       new_list.append({
           'name' : u['name'],
           'avg' : avg
       })
    high_achivers = []

    for m in new_list:
        if m['avg'] >= 75:
            high_achivers.append(m) 
    return high_achivers
    
print(high_scorers(data))

#task 1 - easy way
def task1_easy(data):
    result = []

    for u in data:
        total = u['marks']
        avg = total/len(u['marks'])

        if avg>75:
            result.append({
                'name': u['name'],
                'avg' : avg
            })


#Task 2: Find Topper (Clean Logic Only)

def topper(data):

    new_list = []
    
    for m in data:
        tot = 0
        for i in m['marks']:
            tot += i
        avg = tot/len(m['marks'])
        new_list.append({
            'name':m['name'],
            'avg' : avg
        })
    
    high = new_list[0]
    name = high['name']
    marks = high['avg']

    for x in new_list:
        if x['avg'] > marks:
            marks = x['avg']
            name = x['name']

    return name,marks
print(topper(data))


#🧩 Task 4: Elite Students (Hard)

def elite_students(data):

    result = []
    for u in data:
        total = sum(u['marks'])
        avg = total/len(u['marks'])

        if avg >= 75:
            if all(m>60 for m in u['marks']):
                result.append({
                    'name': u['name'],
                    'avg' : avg
                })
    return result
    
print(elite_students(data))









