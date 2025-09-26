# print("Hello world")
# 1. Factorial with recursions
def fact(i):
    if i > 1:
        return i*fact(i-1)
    else:
        return i
    
c = input("With loops or not (Y/N): ")
i = int(input("Enter the number of which you want to get factorial of: "))

if c=='N' or c =="n":
    print(fact(i))

# 2. Factorial with loops

else:
    t2 = i
    t1 = i
    for a in range(1, t2):
        if t1 > 0:
            t1 = t1 - 1
            i = (i)*(t1)
        else:
            break
    print(i)

# 3. Fibonaci of the numbers
j = int(input("Enter the number: "))
k = 0
print("The series is ")

def fibonacci(k):
    if k <= 1:
        return k
    else:
        return fibonacci(k-1) + fibonacci(k-2)
while(k < j):
    print(fibonacci(k), end=" ")
    k = k+1
