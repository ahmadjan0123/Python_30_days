list1 = [4, 7, 2, 9, 1]

def highest_return(list1):
    highest = -1
    for i in list1:
        if i>highest:
            highest = i
    return highest

print(highest_return(list1))

ch = "Artificial"
def func2(ch):
    counter  = 0
    vowels = ['a','e','i','o','u']
    for i in ch.lower():
        if i in vowels:
            counter+=1
    return counter

print(func2(ch))

list3 = [1,2,3,4,5,6]
def fun3(list3):
    even = []
    for i in list3:
        if i%2==0:
            even.append(i)
    return even

print(fun3(list3))




students = [
    {"name":"Ali","marks":[80,90,70]},
    {"name":"Sara","marks":[90,95,85]},
    {"name":"Ahmed","marks":[60,70,75]}
]

def aver_stu(students):
    avg = 0
    result = {}
    for x in students:
        name = x['name']
        marks = x['marks']

        total = 0
        for s in marks:
            total+=s

        avg = total/len(marks)        

        result[name] = round(avg, 2)
        
    return result


print(aver_stu(students))


def highest_student(students):

    names = aver_stu(students)

    highest_marks = -1
    Highest_name = None

    for x in names:
        if names[x] > highest_marks:
            highest_marks = names[x]
            Highest_name = x
    return Highest_name

print("here ahmad")
print(highest_student(students))



students1 = [
    {"name":"Ali","dept":"AI","marks":[80,90,70]},
    {"name":"Ahmed","dept":"AI","marks":[60,75,85]},
    {"name":"Sara","dept":"DS","marks":[90,88,92]},
    {"name":"Hina","dept":"DS","marks":[70,72,68]}
]

def grp_dep(students1):
    aver_ai = 0
    aver_ds = 0

    total_ai = 0
    total_ds = 0

    output = {
        "AI": 0,
        "DS":0
    }

    count = {
        "AI":0,
        "DS":0
    }

    for x in students1:
        
        dept = x['dept']
        marks = x['marks']

        total = 0
        for s in marks:
            total+= s

        if dept == "AI":
            total_ai += total
            count['AI']+=1
        elif dept == "DS":
            total_ds += total
            count['DS']+=1

        
    aver_ai = total_ai/count["AI"]
    aver_ds = total_ds/count["DS"]

    
    output["AI"] = aver_ai
    output['DS'] = aver_ds

    return output


    

print(grp_dep(students1))


def boss_question(students1):

    aver_ai = {}
    aver_ds = {}
    
    final_output = {
        'AI':{
                "NAME": None,
                "average":0
        },
        'DS':{
                "NAME": None,
                "average":0
        }
    }

    for x in students1:
        name = x['name']
        marks = x['marks']

        total = 0
        for s in marks:
            total+= s

        av = total/len(marks)

        if x['dept'] == "AI":
            aver_ai[name] = av
        elif x['dept'] == 'DS':
            aver_ds[name] = av
    
    
    
    highest_ai = -1
    highest_ds = -1

    for s in aver_ai:
        if aver_ai[s] > highest_ai:
            highest_ai = aver_ai[s]
            final_output["AI"]['name'] = s
            final_output['AI']['average'] = aver_ai[s]

    for t in aver_ds:
        if aver_ds[t]>highest_ds:
            highest_ds = aver_ds[t]
            final_output["DS"]['name']= t
            final_output['DS']['average'] = aver_ds[t]

    return final_output



print(boss_question(students1))
        
