# Not a pythonic approach to solve it
n1 = int(input("Enter Number: "))

r = n1
n1 = n1**2
s = 0
while(r!=0):
    a = r%10
    s = s*10+a
    r = r//10
s = s**2
r = s
s = 0
while(r!=0):
    a = r%10
    s = s*10+a
    r = r//10
if s == n1:
    print("It is an Adam's Number!")
else: 
    print("It isn't an Adam's Number")