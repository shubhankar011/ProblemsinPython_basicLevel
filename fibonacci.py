def fibo(k):
    if k <=1:
        return k
    else:
        return (k-1)+(k-2)

a = int(input("Enter the number of terms you want to be in series: "))
k = 0
for k in range(0, a):
    print("Fibonacci series is: ", fibo(k))