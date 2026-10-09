student = {
    'name': 'Ahmad',
    'age': 19,
    'marks': 85,
    'university': 'IMSciences'
}

print(student['name'])
print(student['age'])

for i in student:
    print(i)

for m in (student):
    print(student[m])


student['marks'] = 90
student['city'] = 'Peshawar'
del student['age']

#if 'age' in student.keys()

print(len(student))




students3 = {
    'names': ['Ahmad', 'Ali', 'Affan', 'Wajeeh'],
    'marks': [85, 62, 91, 48]
}

for i in students3['marks']:
    if i>70:
        print(i)


for i in range(len(students3['marks'])):
    if students3['marks'][i] > 70:
        print(students3['names'][i])


from datetime import datetime

iso_timestamp = '2021-06-23T10:57:17.783Z'

# convert this into data format

dt = datetime.fromisoformat(iso_timestamp)

milli_seconds = (dt.timestamp()*1000)

print(milli_seconds)