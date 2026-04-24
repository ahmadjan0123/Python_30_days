s = "Python"
print(s[0:4])
#print(s[::5])

print("Python" in s)

w = "I love Pizza"

w = w.replace("Pizza","Burger")
print(w)

print("TASK 1")
s1 = "I love Python"
print(s1[::-1])

print("\nTask 3")
s2 = "python is FUN   "
print(s2.title())

print("\nTask 2")
s3 = "Python is powerful and easy"
s3.strip()
counter = 0
for q in s3:
    counter +=1
print(f'THe number of words is: {counter}')