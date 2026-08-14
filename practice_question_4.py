import pandas as pd
import numpy as np

data = {
    "Student": ["Ali", "Sara", "Ahmed", "Usman", "Ayesha", "Hamza", "Zain"],
    "Age": [20, 21, 19, 45, 22, 20, 19],
    "Study_Hours": [5, 7, 4, 2, 50, 6, 3],
    "Score": [78, 91, 65, 72, 95, 82, 60]
}

df = pd.DataFrame(data)

print(df[(df['Age']>30) | (df['Study_Hours']>15)])


data1 = {
    "Student": ["Ali", "Sara", "Ahmed", "Usman", "Ayesha", "Hamza"],
    "Score": [82, 95, 76, 88, 91, 69]
}

df1 = pd.DataFrame(data1)

df1 = df1.sort_values('Score',ascending=False)

df1['rank'] = df1['Score'].rank(method='dense',ascending=   False).astype(int)


A = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])


print(A*B)

print(A@B)

print(A.T)




data3 = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop"],
    "Units": [5, 12, 7, 8, 15, 4, 10],
    "Price": [1000, 600, 400, 1000, 600, 400, 1000]
}

df3 = pd.DataFrame(data3)


df3['Revenue'] = df3['Units']* df3['Price']


print(df3.groupby('Product')['Revenue'].sum())