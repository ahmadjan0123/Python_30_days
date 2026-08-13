numbers = [12, 7, 25, 30, 18, 41, 9, 50, 64, 15]

list1 = [x for x in numbers if x%2==0 and x>20]
print(list1)

import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Age": [20, 25, 19, 30, 22],
    "Marks": [75, 88, 92, 65, 81],
    "City": ["Peshawar", "Islamabad", "Lahore", "Peshawar", "Islamabad"]
}

df = pd.DataFrame(data)

print(df[(df['Marks']>80) & (df['City']=='Islamabad')])



print(df['Marks'].mean())
print(df['Marks'].max())
print(df['Marks'].min())
print(df['Age'].mean())


print(df.groupby('Marks')['City'])






