# n = int(input("Enter the integer: "))
# s = 0
# i = 0
# while n!=0:
#     a = n%10
#     s = s + a
#     n = n//10
#     i += 1
# print(f"The sum of digits is: {s} and the number of digits is {i}")
n = input("Enter the integer: ")
a = 0
for i in range(0, len(n)):
    a = a + int(n[i])
print(f'The sum of digits is: {a} and the number of digits is {len(n)}')