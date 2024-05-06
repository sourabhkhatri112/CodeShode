############### 2 ways to define FLOAT ####################
myFloat = 7.0
print(myFloat)

myFloat = float(7)
print(myFloat)
###########################################################
a, b = 3, 4
print(a, b)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
fullName = hello + world
print(fullName)

''' MIXING OPERATORS LIKE BELOW IS NOT SUPPORTED
fullWord = one + two + fullName
print(fullWord)
'''
###########################################################

mystring = "hello"
myfloat = None
myint = None

if mystring == "hello":
    print("String: %s " % mystring)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
