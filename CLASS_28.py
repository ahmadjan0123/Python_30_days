l1 = "AI,Python,Machine Learning"
print(l1.split())

l2 = ["I", "love", "Python"]
print(" ".join(l2))

#text1 = input('enter your 3 hobbies')

#print(text1.split())

#text2 = input('enter your senetence: ')
#print(text2.replace(" ","_"))

first_name = 'ahmad'
last_name = 'jan'
print(f"{first_name} {last_name}")

text3 = "apple|banana|mango|orange"
print(text3.split('|'))

text4 = "my name is ahmad"
print("|".join(text4.split()))

input1 = input('enter your recors').split()

words = [word for word in input1 if word.isalpha()]
marks = [int(x) for x in input1 if x.isdigit()]

names = " ".join(words)

if marks:
    print('average is: ',sum(marks)/len(marks))
else:
    print('marks not available')





para = input('enter the paragraph: ')

def task_11(para):
    words = para.split()
    rep = para.replace(" ","_")
    t_case = para.title()

    long_string = words[0]

    # PROGRAM FOR LONGEST WORDS
    for x in words:
        #print(len(x))
        if len(x) > len(long_string):
           
           long_string = x
    
    # PROGRAM FOR SHORTEST WORD


    shortest_word = words[0]
    for t in words:
        if len(t) < len(shortest_word):
            shortest_word = t



    print(words)
    print(len(words))
    print(rep)
    print(t_case)
    print('longest word: ',long_string)
    print('shortest word:',shortest_word)

task_11(para)



input3 = input("enter your data: ").split(',')
def task13(input3):
    print('name: ',input3[0])
    print('Phone Number: ',input3[1])
    print('E-mail: ',input3[2])



task13(input3)
