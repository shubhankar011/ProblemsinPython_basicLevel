# import random

password = "shubh"
l_Capital = []
l_small = []
for i in range(65, 91):
    l_Capital.append(chr(i)) # It has to use character encoding not the string typecasting although the type or class of the variable is going to be in string.

for i in range(97, 123):
    l_small.append(chr(i))
print(l_Capital,"\n",l_small)