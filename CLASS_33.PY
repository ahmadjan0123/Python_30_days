def student_report(data):
    final_result = {}

    for x in data:
        name= x
        marks = data[x]
        
        avg =0
        for a in marks:
            avg += a
        avg = round(avg/len(marks),2)

        
        highest_socre = marks[0]

        for s in marks:
            if s>highest_socre:
                highest_socre = s
        lowest_marks = marks[0]
        for e in marks:
            if e<lowest_marks:
                lowest_marks = e

        garde = None

        if avg>=90:
            grade = 'A'
        elif avg>=80:
            grade = 'B'
        elif avg>=70:
            grade = 'C'
        elif avg>=60:
            grade = 'D'
        else:
            grade = 'F'      
        final_result[name]    = {
        'average': avg,
        'highest_score': highest_socre,
        'lowest_score':lowest_marks,
        'grade': grade
    }

    return final_result


students = {
    "Ali": [85, 90, 78],
    "Sara": [92, 88, 95],
    "John": [60, 72, 68]
}
print(student_report(students))


sales = {
    "Laptop": [50000, 55000, 52000],
    "Phone": [30000, 31000, 29500],
    "Tablet": [20000, 21000, 20500]
}

def sales_report(data):
    final_result = {}
    
    for x in data:
        name = x
        price = data[x]

        total = 0
        avg = 0
        for s in price:
            total+=s
        avg = round(total/len(price),2)


        highest_price = price[0]
        lowest_price = price[0]

        for h in price:
            if h>highest_price:
                highest_price = h
        
        
        for t in price:
            if t<lowest_price:
                lowest_price = t


        # for the trend one

        
        if   price[-1]>price[0]:
            trend = 'increasing'
        elif   price[-1]<price[0]:
            trend = 'decreasnig'
        else:
            trend = 'stable'


        final_result[name] = {
            'TOTAL': total,
            'AVERAGE':avg,
            'highest':highest_price,
            'lowest':lowest_price,
            'trend':trend
        }
        
    return final_result
print(sales_report(sales))


employees = {
    "Ali": {
        "department": "AI",
        "tasks": [8, 10, 9, 7]
    },
    "Sara": {
        "department": "Web",
        "tasks": [9, 9, 10, 10]
    },
    "John": {
        "department": "AI",
        "tasks": [6, 7, 8, 6]
    },
    "Ayesha": {
        "department": "Data",
        "tasks": [10, 9, 10, 9]
    }
}

def employee_report(data):
    final_result = {}
    for x in data:
        name = x
        dept = data[x]['department']
        tasks = data[x]['tasks']

        total = 0
        average = 0

        for s in tasks:
            total+=s
        average = total/len(tasks)

        highest_week = tasks[0]
        lowest_week = tasks[0]
        for h in tasks:
            if h>highest_week:
                highest_week = h
        
        for l in tasks:
            if l<lowest_week:
                lowest_week = l

        if average>=9:
            perfromace = 'Excellent'
        
        elif average>=8:
            perfromace = 'Good'
        
        elif average>=7:
            perfromace = 'Average'
        
        else:
            perfromace = 'Poor'

        final_result[name]={
        'department':dept,
        'total tasks':total,
        'average tasks':average,
        'highest_week':highest_week,
        'lowest_week':lowest_week,
        'Performace':perfromace
    }
    return final_result







print(employee_report(employees))