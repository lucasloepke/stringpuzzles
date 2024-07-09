# Solutions to PYnative's python string exercise
# https://pynative.com/python-string-exercise/

# 1A, 1B
""" word = input("Enter a word: ")
mid = int(len(word)/2)
newstr = word[:1] + word[mid] + word[-1:]
newerstr = word[mid-1:mid+2]
print(str.capitalize(word)+" has become "+newstr+" and "+newerstr) """

# 2, 3
""" str1 = input("Enter first word: ")
str2 = input("Enter second word: ")
mid = int(len(str1)/2)
print("Posit this! " + str1[:mid] + str2 + str1[mid:] + " and " + str1[:1] + str2[:1] + str1[mid] + str2[int(len(str2)/2)] + str1[-1:] + str2[-1:]) """

# 4
""" word = input("Enter a word: ")
newstr = ""
for i in word:
    if i.islower():
        newstr = newstr + i
for i in word:
    if i.isupper():
        newstr = newstr + i
print(newstr) """

# 5
""" str1 = "P@#yn26at^&i5ve"
chars = 0; digits = 0; symbols = 0
for i in str1:
    if i.isalpha():
        chars = chars + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        symbols = symbols + 1
print("Chars: "+str(chars) + "\nDigits: "+str(digits) + "\nSymbols: "+str(symbols)) """

# 6
""" s1 = "Abc"; s2 = "Xyz"; s3 = ""
length = len(s1) if len(s1) > len(s2) else len(s2)
s2 = s2[::-1]
for i in range(length):
    if i < len(s1):
        s3 = s3 + s1[i]
    if i < len(s2):
        s3 = s3 + s2[i]
print(s3) """

# 7
""" def test(s1, s2):
    check = True
    for i in s1:
        if not s2.__contains__(i):
            check = False
            print(s1+" and "+s2+" are not balanced")
            return
    print(s1+" and "+s2+" are balanced")
test("Yn", "PYnative")
test("Ynf", "PYnative") """

# 8
""" str1 = "Welcome to USA. usa awesome, isn't it? uSA"
str2 = "usa"
count = 0
for i in range(len(str1)-2):
    if str1[i].lower() == "u":
        if str1[i+1].lower() == "s":
            if str1[i+2].lower() == "a":
                count = count + 1
print("The "+str2+" count is "+str(count)) """

# 9
""" str1 = "PYnative29@#8496"
count = 0; runtot = 0
for i in str1:
    if i.isdigit():
        runtot += int(i)
        count = count + 1
print("Sum is "+str(runtot)+". Average is "+str(runtot/count)) """

# 10
""" str1 = "Apple"
dict = {}
for i in str1:
    count = str1.count(i)
    dict[i] = count
print(dict) """

# 11
""" str1 = "PYnative"
print(str1[::-1]) """

# 12
""" str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1.rindex("Emma")) """

# 13
""" str1 = "Emma-is-a-data-scientist"
print(str1.replace('-', '\n')) """

# 14
""" str1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(list(filter(None, str1))) """

# 15
""" import re
str1 = "/*Jon is @developer & musician"; str2 = ""
str1 = re.sub(r'[^a-zA-Z\s]', '', str1)
str1 = re.sub(r' +', ' ', str1)
print(str1) """

# 16
""" import re
str1 = 'I am 25 years and 10 months old'
str1 = re.sub(r'[\D]', '', str1)
print(str1) """

# 17
""" from itertools import compress
str1 = "Emma25 is Data scientist50 and AI Expert"
elements = str1.split(sep=' ')
alpha = [False if i.isalpha() else True for i in elements]
print(list(compress(elements, alpha))) """

# 18
""" import re
str1 = '/*Jon is @developer & musician!!'
str1 = re.sub(r'[^a-zA-Z\s]', '#', str1)
print(str1) """

# To be added:
# Python equivalent of switch statement to choose which problem to run view.