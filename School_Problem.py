v = {  
    "Shubhankar":"Coder & Student",
    "Raghvendra":"Teacher"
}

# print(v[0]) -- Gives error as indexing is not valid in dictionary
items = list(v.items())
print(items[0],"\nThe length of dictionary is: ",len(items),"\n")


if "Anurag" in v:
    print(v["Shubhankar"])
else:
    print(v["Raghvendra"])
for i in range(0, len(items)):
    print(items[i])

# a = int(input("Enter the first no.:"))
# b = int(input("Enter the second no.:"))
# c = int(input("Enter the third no.:"))

# for i in range(0,len(v)):
#     print(v[i])

'''
p = a>b and a>c
e = b>a and b>c

if p==True:
    print(f"{a} is largest among others")
elif e==True:
    print(f"{b} is largest among others")
else:
    print(f"{c} is largest among others")

if a>b and a>c:
    print(f"{a} is larger among others")
elif b>c and b>a:
    print(f"{b} is larger among others")
elif a==b and a==c:
    print(f"{a}, {b}, {c} are equal")
else:
    print(f"{c} is larger among others")
'''