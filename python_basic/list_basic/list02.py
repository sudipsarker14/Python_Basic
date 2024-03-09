list = [1, 'str', 41, 50.6,['sdp', 40, 6.1]]

t=len(list)

print(t)
#print list using for
for a in list:
    print(a)

print()
#print list using for loop range
    
for a in range(t):
    print(list[a])

print()
#print reverse order using loop
for a in range(t-1,-1,-1):
    print(list[a])