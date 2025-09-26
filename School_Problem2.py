import random
l = [0,1,2,3,4,5,6]
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
a = int(input("Enter the number: "))

# Linear Search Algorithm
if a in l:
    for i in range(0, len(l)):
        if a == l[i]:
            print(f"According to your number: {week[i-1]}")
            break
        else:
            print("Searching...")
else:
    print("You've entered wrong number, try again")