#string advanced

# Anagram Checking

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print('true')
else:
    print('false')

count_word1 = {}
count_word2 = {}

for x in word1:
    if x in count_word1:
        count_word1[x]+=1
    else:
        count_word1[x] = 1
print(count_word1)

for x in word2:
    if x in count_word2:
        count_word2[x]+=1
    else:
        count_word2[x] = 1


if count_word1 == count_word2:
    print('they are same \nAnargam')
else:
    print('not anargam')


def check_anagram(w1,w2):
    freq1 = {}
    freq2 = {}

    for x in w1:
        if x in freq1:
            freq1[x]+=1
        else:
            freq1[x]=1
    
    for x in w2:
        if x in freq2:
            freq2[x]+=1
        else:
            freq2[x]=1
    

    if (freq1 == freq2):
        print(f"{w1} is the  same as {w2}")
    else:
        print(f'{w1} is not the same as {w2}')

check_anagram('earth','hearth')
check_anagram('apple','paple')
check_anagram('cat','dog')

def check_anagram2(w1,w2):

    if len(w1) != len(w2):
        return False
    freq = {}

    for x in w1:
        if x in freq:
            freq[x]+=1
        else:
            freq[x] = 1

    for x in w2:
        if x in freq:
            freq[x]-=1
        else:
            freq[x]+=1

    for x in  freq.values():
        if x != 0:
            return False
        
    return True


print(check_anagram2('listen','silent'))



def rle(text):

    current_char = text[0]
    count = 1
    encoded_string = ""

    for x in text[1:]:
        if x==current_char:
            count+=1
        else:
            encoded_string+= current_char+str(count)
            current_char = x
            count = 1
        
    
    encoded_string += current_char+str(count)
    return encoded_string

print(rle('AAABBCCD'))













