# n = int(input("Enter the integer: "))
# s = 0
# i = n
# while n!=0:
#     a = n%10
#     s = s + (a**3)
#     n = n//10
# if i == s:
#     print("It is an armstrong number!")
# else:
#     print("It isn't an armstrong number!")

n = input("Enter the number: ")
a = 0
for i in range(0, len(n)):
    a = a + (int(n[i])**3)
if a == int(n):
    print("It is an Armstrong number")
else:
    print("It isn't an Armstrong Number!")