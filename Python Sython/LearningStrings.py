name = "John"
print("Hello, %s" % name, "Wick")  # 1st method to print the string
print(f"Hello, {name} Wick")  # 2nd method to print the string
print("Hello,", name, "Wick")  # 3rd method to print the string

print("##########################################################################")
name = "John"
age = 23
print("%s" % name, f"is {age} years old")  # using 1st & 2nd string method together
print(len(name))  # Used to print length

print("##########################################################################")

myList = [1, 2, 3]
print("A list is %s" % myList)  # You can also print the whole list together

print("##########################################################################")

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."  # You can print all data from array in sequence also
print(format_string % data)
print("##########################################################################")

astring = "Hello World"
print(astring.index("o"))  # To print a specific index
print(astring.count("l"))  # To count occurrence of a specific string
print(astring[3:7])  # Print all the character from [3 to 6]...last 7 is skipped
print(astring[3:7:1])  # Yields the same result as above
print(astring[::-1])  # Reverse string
print(astring.upper(), astring.lower())  # TO UPPERCASE & lowercase
print(astring.startswith("Hello"), astring.endswith("World"))  # Provides true in both conditions
print(astring.split(" "))  # seperate string from the space(" ")

print("##########################################################################")

str = "Strings are awesome!"
print("Lenght of s is %d" % len(str))
print("First occurrence of letter a is %d" % str.index("s"))
print("First five characters are %s" % str[:5])  # Print first five characters in string
print("Next five characters %s " % str[5:10])   # Print next five characters in string
print("Characters with odd index %s" %str[1::2])    # Printing odd indexes
print("Characters at last 5 index %s" %str[-5:])    # -5 means END SE 5 peeche

print("######################### STRING SPLITTING ##############################")

print("Splitting %s" %str.split(" ",2))

print("##########################################################################")