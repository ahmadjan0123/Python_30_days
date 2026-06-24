word = "ahmad"

counter = 0
for ch in word:
    counter+=1

print(counter)

# count alphabets only  - using .isalpha()

w2 = "ahmad123"
count1 = 0
for x in w2:
    if x.isalpha():
        count1+=1
print(count1)

# count digits only  - using .isdigit()

w3 = "ahmas321"
count2 = 0

for r in w3:
    if r.isdigit():
        count2+=1

print(count2)

#count blank spaces 


w4 = "ahmad is top ai engineer"
count4 = 0
for s in w4:
    if s==" ":
        count4+=1
print("the number of null spaces is:",count4)


# freq counter 
freq1 = 'banana'

freq11= {}

for x in freq1:

    if x  not in freq11:
        freq11[x] = 1

    else:
        freq11[x]+=1

print(freq11)


# freq counter with maximum

freq2 = 'engineer'
freq22= {}

for x in freq2:
    if x not in freq22:
        freq22[x] = 1
    else:
        freq22[x]+=1

highest_name = None
highest_score = -1


for z in freq22:
    if freq22[z] > highest_score:
        highest_score = freq22[z]
        highest_name = z

print("highest name: ",highest_name)
print("highest_score: ",highest_score)


# TEST CODES
# test number 1 : characters

text = "Artificial Intelligence"
counter = 0
for x in text:
    counter+=1
print(counter)


# test number 2: Count alphabets only.

text1 = "AI2026!"
counter1 = 0
for x in text1:
    if x.isalpha():
        counter1+=1
print(counter1)


#test code number 3: count digits only
text2 = "AI2026!"
counter2 = 0

for s in text2:
    if s.isdigit():
        counter2+=1

print(counter2)

#test code number 4: Build frequency dictionary.

word1 = "mississippi"
word1_dict = {}

for x in word1:
    if x not in word1_dict:
        word1_dict[x] = 1
    else:
        word1_dict[x]+=1
print(word1_dict)



#test code number 5: Find the most frequent character.
word2 = "programming"
word2_dict = { }

for d in word2:
    if d not in word2_dict:
        word2_dict[d] = 1
    else:
        word2_dict[d]+=1

high_name = None
high_score = -1

for x in word2_dict:
    if word2_dict[x] > high_score:
        high_score = word2_dict[x]
        high_name = x

print("Highest name: ",high_name)
print("Highest_score: ",high_score)






word3 = "Artificial"

counter_vow = 0
for x in word3.lower():
    if x in "aeiou":
        counter_vow+=1
print(counter_vow)

counter_con = 0

for x in word3.lower():
    if x.isalpha() and x not in "aeiou":
        counter_con+=1
print(counter_con)















