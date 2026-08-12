numbers = [12, 7, 25, 30, 18, 41, 9, 50]

list1 = [x for x in numbers if x%2==0 and x>20]
print(list1)


import pandas as pd



data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [20, 25, 19, 30, 22],
    "Marks": [85, 72, 91, 65, 88]
}

df = pd.DataFrame(data)
print(df)

print(df['Age']>=20)
print(df['Marks']>80)

print(df[(df['Marks']>80)& (df["Age"]>=20)])

#task - 3
print(df['Marks'].mean())
print(df['Marks'].mean())
print(df['Marks'].max())
print(df['Marks'].min())

data1 = {
    "Department": ["AI", "AI", "CS", "CS", "AI", "SE", "SE", "CS"],
    "Student": ["Ali", "Sara", "Ahmed", "Usman", "Ayesha", "Hamza", "Zain", "Bilal"],
    "Marks": [85, 92, 78, 88, 95, 72, 81, 90]
}

df1 = pd.DataFrame(data1)

print(df1.groupby('Department')['Marks'].mean())