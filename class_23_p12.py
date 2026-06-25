#example 1
def count_cases(word1):
    count = {
        "upper_case": 0,
        "lower_case": 0
    }
    for x in word1:
        if x.isupper():
            count['upper_case']+=1
        elif x.islower():
           count['lower_case']+=1
    return count

print(count_cases("pyThon"))


# example 2
def case_report(text):
    count1 = {
        'upper_case':0,
        'lower_case':0,
        'digit_count':0
    }

    for x in text:
        if x.isupper():
            count1['upper_case']+=1
        elif x.islower():
            count1['lower_case']+=1
        elif x.isdigit():
            count1['digit_count']+=1
    return count1

print(case_report("AI2026RockS"))



# reverse string



def reverse_string(text):
    reversed_string  = ""
    for ch in text:
        reversed_string = ch +  reversed_string 

    return reversed_string

print(reverse_string("AHMAD"))


def is_palindrome(text):
    ans = True    
    reversed_string = ""
    for ch in text:
        reversed_string = ch + reversed_string

    if text == reversed_string:
        ans = True
    else:
        ans = False

    return ans

print(is_palindrome('ahmad'))