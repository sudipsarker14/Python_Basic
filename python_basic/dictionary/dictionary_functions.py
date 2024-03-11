d ={
    'name' : 'python',
    'fee' : '8000',
    'duration' : '2 months'
}

c = d.get('name')
print(c)
print()
for a in d.keys():
    print(a)

print()
for a, b in d.items():
    print(a, b)
print()
del d['fee']
print(d)

print()
d.pop('duration')
print(d)
print()
d = dict(name= 'java', fee= '10000')
print(d)
print()
d.update({'fee': 10000})

print()
d.clear()
print(d)

d ={
    'name' : 'python',
    'fee' : '8000',
    'duration' : '2 months'
}

d['name'] = 'sudip'
print(d)