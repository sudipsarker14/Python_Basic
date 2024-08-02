course = {
    'php' : {'duration' : '3 Months', 'fees' : 15000},
    'java' : {'duration' : '2 Months', 'fees' : 10000},
    'python' : {'duration' : '2 Months', 'fees' : 12000},
}

print(course)
print(course['php']['duration'])

for k,v in course.items():
    print(k,v['duration'], v['fees'])