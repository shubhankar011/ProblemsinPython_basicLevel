import random

n = int(input("Enter the number of which you want square root of: "))
g = random.randint(0,n)

while True:
    g = (g + n/g) / 2

    if abs(g*g - n) < 1e-6:
        break
print("Approximate sqrt:", g)
print("Integer sqrt:", int(g))
#  Comment out the first, if you want to use the second
# import random

# n = int(input("Enter number: "))
# g = random.randint(0, n)

# while True:
#     if g**2 == float(n):
#         break
#     elif abs(g*g - n) == 0 or abs(g*g - n) < 1e-6:
#         break
#     else:
#         g = (g + (n/g))/2
#         print(g)

