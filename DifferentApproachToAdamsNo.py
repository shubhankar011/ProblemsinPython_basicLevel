def reversing(n1):
    return int(str(n1)[::-1])
def checking(n1, n2):
    if (n1**2)==(reversing(n2**2)):
        return True
    else:
        return False
n1 = int(input("Enter a number: "))
n2 = reversing(n1)
print(n2)
print(f"It is {'an' if checking(n1,n2) == True else 'not an'} Adams Number")
# if checking(n1,n2)==True:
#     print("It is an Adams Number! ")
# else:
#     print("It isn't an Adams Number!")