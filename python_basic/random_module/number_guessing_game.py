import random

cnumber = random.randrange(1, 101)
UserInput = int(input("Enter your Number:--- "))
if UserInput<cnumber:
    print("Computer Number", cnumber)
    print('Your guess number is too low')

elif UserInput>cnumber:
    print("Computer Number", cnumber)
    print("Your guess number is too big")

else:
    print("compter number", cnumber)
    print("Your guess number is equal")