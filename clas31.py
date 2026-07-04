#split without the split function

def split1(text):

    l1 = []
    char = ""

    for x in text:
        if x!=" ":
            char+=x
        else:
            l1.append(char)
            char = ""
    l1.append(char)

    return l1

print(split1('ahmad is writing code in pyhton'))

def split2(text,seperator):

    l2 = []
    char = ""

    for x in text:
        if x!=seperator:
            char+=x
        else:
            l2.append(char)
            char = ""

    l2.append(char)

    return l2

print('ahmad-is-plainnig-to-eat-mangoes','-')


def join1(text):
    char = ""
    string = ""

    for x in text:
        if x!=",":
            char+=x + " "

        else:
            string =string + char 
            char = " "

    string = char + string

    return string
 
print(join1(['ahmad','is','a','programmer']))


def join2(text,join):
    char = ""
    string = ""

    for x in range(len(text)):
        
        if x!= (len(text)-1):
            char += text[x] + join
        else:
            char += text[x]
        
        #print(f'{x}:{text[x]}')

    return char
    



print(join2(['i','love','ai'],'-'))







