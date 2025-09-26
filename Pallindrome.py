n1 = int(input("Enter a number: "))
# Reversing the number
'''s = 0
while n1!=0:
    a = n1%10
    s = s*10+ a
    n1 = n1 // 10
print(s)'''
s = int(str(n1)[::-1])
# print(s, type(s))
if s == n1:
    print("It is pallindrome!")
else:
    print("It isn't pallindrome")