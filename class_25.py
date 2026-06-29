#Day 1: Python String Methods & Searching

name = "  i love banana           "

print(name.strip())

print(name.lstrip())
print(name.rstrip())


text = 'i want bubble'
t1 = text.replace('bubble','chocolate')
print(t1)

print(text.split())
print(name.split())

l1 = ['a','b','c']

print(('-'.join(l1)))


email = "admin@gmail.com"
print(email.startswith('admin'))
print(email.endswith('.comm'))


print(name.find('love'))

print(name.find('strawbwery'))


text1 = 'banana'
print(text1.count('a'))

print('bubble' in text)


#question - 1 
text = "PyTHon ProGRAMMING"
print(text.lower())

#question - 2
text1 = "      AI Student      "
print(text1.strip())

#question - 3
text = "My cat chased another cat."
print(text.replace('cat','dog'))

#question - 4
sentence = input('enter a sentecne:')

print(sentence.lower().count('e'))

#question - 5
sentence1 = input('enter the email:')

if sentence1.lower().endswith('.com'):
    print('valid')
else:
    print('invalid')

#question - 6

sentence2 = input('enter the sentece: ')

spp = sentence2.split()
print(len(spp))


#task 7
#para = input('enter the paragraph: ')

def task7():
    para = input('enter the paragraph: ')
    words = para.split()
    char = para.replace(" ","")
    commas = para.count(',')
    full_stop = para.count('.')


    print('total numbers of words: ',len(words))
    print('total number of characters: ',len(char))
    print("commas: ",commas)
    print('full stop: ',full_stop)

task7()



