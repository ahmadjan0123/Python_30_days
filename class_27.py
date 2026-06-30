password = "Python2026"
print(password.isalnum())


name = 'ahmad'
age = 20

print(f"my name is {name} and age is {20}")

print('my name is {} and my age is {}'.format(name,age))




text = "Ai"

print(f"|{text:>15}|")
print(f"|{text:<15}| ")

student_id = "Ai12345678"

if student_id.startswith("Ai"):
    if len(student_id) == 10:
        if student_id[2:].isdigit():
            print('ID Valid')
else:
    print('ID not valid')


word = "Ahmad"
word = word.lower()
vowel = 0

for x in 'aeiou':
    vowel += word.count(x)

print(vowel)
        

