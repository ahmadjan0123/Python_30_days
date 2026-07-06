

def q1(text,join = "*"):

    result = ""
    
    for x in range(len(text)):
        if x!= (len(text)-1):
             result += text[x]+join
    else:
            result += text[x]
            print()
    return result

print(q1(['ahmad','is','a','good','programmer'],","))


def q2(text,join):
     
    result = ""
    neww = []
    for x in text:
          neww.append(str(x))
    print(neww)


    for s in range(len(neww)):
        if s!= (len(neww)-1):
               result += neww[s] + join
        else:
             result += neww[s]

    return result



print(q2([1,2,3,4],'~'))


def q3(text,join):
     
    new_words = []
    result = ""

    for x in text:
          if len(x)>3:
               new_words.append(x)
    for s in range(len(new_words)):
        if s!= (len(new_words)-1):
             result += new_words[s] + join
        else:
             result += new_words[s]
    return result    

print(q3(["AI","Machine","Deep","ML","Learning"],'-'))


def q4(text,join):
   
    reverse_list = []
    result = ""

    for i in range(len(text)-1, -1, -1):
         reverse_list.append(text[i])
   
   
   

    for x in range(len(reverse_list)):
        if x!= (len(reverse_list)-1) and x!=" ":
              result+= reverse_list[x]+join
        else:
             result += reverse_list[x]

    return result
print(q4(["I","Love","Python"],','))


def q5(text,join):
    result = ""
    for x in range(len(text)):
        if x!= (len(text)-1):
            result += text[x] + join
        else:
            result += text[x]
    return result


print(q5(['1','2','3'],'-'))