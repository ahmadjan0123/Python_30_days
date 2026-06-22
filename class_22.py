students = [
    {"name": "Ali", "dept": "AI", "marks": [80, 90, 70]},
    {"name": "Ahmed", "dept": "AI", "marks": [60, 75, 85]},
    {"name": "Sara", "dept": "DS", "marks": [90, 88, 92]}
]

# TASK - 1 

def student_averages(students):
    avg_dict = {}
    for x in students:
        name = x['name']
        marks = x['marks']

        total = 0
        for s in marks:
            total += s
        avg = total/len(marks)

        avg_dict[name] = avg
    return avg_dict

print(student_averages(students))


# TASK - 2 

def best_student(students):

    names = student_averages(students)
    best_name = None
    Highest_Marks = -1


    for x in names:
        if names[x] > Highest_Marks:
            best_name = x
            Highest_Marks = names[x]

    return best_name



print(best_student(students))


# TASK - 3
def department_average(students):

    count = {
        "AI":0,
        "DS":0
    }
    avg_ai = 0
    avg_ds = 0

    for x in students:

        dept = x['dept']
        marks = x['marks']

        total = 0
        for s in marks:
            total += s 

        if dept == "AI":
            avg_ai+=total
            count["AI"]+=1
        elif dept == 'DS':
            avg_ds += total
            count["DS"] += 1

    avg_ai/= count["AI"]
    avg_ds /= count["DS"]

    result = {
        "AI": avg_ai,
        "DS":avg_ds
    }

    return result


print(department_average(students))
            

# TASK - 4

def all_marks(students):
    all_score = []
    for x in students:
        for s in x['marks']:
            all_score.append(s)
    return all_score

print(all_marks(students))



# TASK - 5

def top_per_department(students):

    Ai = {
        'name' :None,
        'average':-1
    }
    Ds = {
        'name':None,
        'average':-1
    }

    for x in students:
        name = x['name']
        dept = x['dept']
        marks = x['marks']

        total = 0
        avg = 0
        for t in marks:
            total+=t
        avg = total/len(marks)
        if dept == "AI":
            if avg > Ai["average"]:
                Ai["average"] = avg
                Ai["name:"] = name
        elif dept == "DS":
            if avg > Ds["average"]:
                Ds["average"] = avg
                Ds["name"] = name

    result = {
        "AI": Ai["name: "],
        'Ds': Ds["name"]

    }

            
    return result


        



                

print(top_per_department(students))

        


        


