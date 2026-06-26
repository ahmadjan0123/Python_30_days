
name = "I am ahmad yousuf jan"

new_word = ""

for x in name:
    if x==" ":
        new_word += "_"
    else:
        new_word+=x

print(new_word)

#removing digits from a string

name1 = "abcd!!23556tyui"
new_word1 = ""
for s in name1:
    if not s.isdigit():
        new_word1 += s

print(new_word1)

# removing all the other values other than characters

name2 = "ahmad 123 !!!! 01233"
new_word2 = ""

for t in name2:
    if t.isalpha():
        new_word2+=t

print(new_word2)

# upper case to lower and vice versa - manually 

name3 = "a"

code = ord(name3)
print(code)

if  97>= code <=122:
    code-=32

print(chr(code))


name4 = 'D'
code1 = ord(name4)

if 65>= code1<=90:
    code1+=32

print(chr(code1))

text1 = "Hello"
new_num = 0
new_name = ""
for t in text1:
    
    code2 = ord(t)
    if  97<=code2<=122:
        new_num =code2 -  32
        new_name = new_name + chr(new_num)
    else:
        new_name = new_name + chr(code2)

print(new_name)

