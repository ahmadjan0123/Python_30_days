# DICTATINORY
 
dic1 = {
    "name": "ahmad",
    "marks" : 56,
    "subject" : "english"
}
dic1['city'] = "peshawar"
dic1["marks"] = 98

#print(dic1["marks"])

dic2 = {

    "color"   : "green",
    "2Dshape" : "circle",
    "3Dshape" : "cuboid"

}

for i in dic2:
    print(i,dic2[i])
print("   ")


#task 1
task1 = {
    "name" : "macroni",
    "price": 250,
    "quantity" : 4
}

#task 2
car = {"brand": "Toyota", 
       "year": 2020
    }
car['color'] = 'black'
car['year'] = 2022

for key in car:
    print(key,car[key])

#task 3
marks = {"math": 80, "physics": 70, "cs": 90}

total = 0
for m in marks:
    total += marks[m]

print(total)
print(" ")

#task 4
students1 = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78
}

h1 = list(students1.values())[0]
highest_name = list(students1.keys())[0]

for m in students1:
    if  students1[m] > h1:
        h1 = students1[m]
        highest_name = m

print(f"The highest marks are of {highest_name} , marks are {h1}")

#lowest marks finding
l1 = list(students1.values())[0]
lowest_name = list(students1.keys())[0]

for t in students1:
    if  students1[t] < l1:
        l1 = students1[t]
        lowest_name = t

print(f"The lowest marks are of{lowest_name}, marks are {l1}")






#nested Dictionaries
info = {

    "Ali" :{
        "age" : 18,
        "city" : "peshawar"
    },
    "Ahmad" : {
        'age' : 19,
        "city" : "charsadda"
    },
    "Mobeen" :{
        'age':20,
        "city":"Kabul"
    }
}

print(info['Ali']['age'])

students2= {
    "Ali": {
        "age": 18,
        "marks": 85
    },
    "Ahmed": {
        "age": 19,
        "marks": 92
    },
    "Sara": {
        "age": 18,
        "marks": 78
    }
}

#task 1

print(f"The student age is: {students2['Ahmed']['age']}")
print(f"Sara's marks are: {students2['Sara']['marks']}")

#task 2
tot = 0

for r in students2:
    tot += students2[r]['marks']

print(tot)

#task 3
hh1 = list(students2.values())[0]['marks']
name = list(students2.keys())[0]


for e in students2:
    if students2[e]['marks'] > hh1:
        hh1 = students2[e]['marks']
        name = e


print(f"In nested the highest marks are of {name} which are{hh1}")

# task 4

for a in students2:
    if students2[a]['marks'] > 80:
        print(a)