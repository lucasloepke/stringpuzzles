# Solutions to PYnative's python string exercise
# https://pynative.com/python-string-exercise/

import re
from itertools import compress

def run(x, all):
    # 1A, 1B
    if (x == 1 or all is True):
        word = "JhonDipPeta"
        mid = int(len(word)/2)
        newstr = word[:1] + word[mid] + word[-1:]
        newerstr = word[mid-1:mid+2]
        print(word+" has become "+newstr+" and "+newerstr)

    # 2, 3
    if (x == 2 or x == 3 or all is True):
        str1 = "America"
        str2 = "Japan"
        mid = int(len(str1)/2)
        print("Posit this! " + str1[:mid] + str2 + str1[mid:] + " and " + str1[:1] + str2[:1] + str1[mid] + str2[int(len(str2)/2)] + str1[-1:] + str2[-1:])

    # 4
    if (x == 4 or all is True):
        word = "PyNaTive"
        newstr = ""
        for i in word:
            if i.islower():
                newstr = newstr + i
        for i in word:
            if i.isupper():
                newstr = newstr + i
        print(newstr)

    # 5
    if (x == 5 or all is True):
        str1 = "P@#yn26at^&i5ve"
        chars = 0; digits = 0; symbols = 0
        for i in str1:
            if i.isalpha():
                chars = chars + 1
            elif i.isdigit():
                digits = digits + 1
            else:
                symbols = symbols + 1
        print("Chars: "+str(chars) + "\nDigits: "+str(digits) + "\nSymbols: "+str(symbols))

    # 6
    if (x == 6 or all is True):
        s1 = "Abc"; s2 = "Xyz"; s3 = ""
        length = len(s1) if len(s1) > len(s2) else len(s2)
        s2 = s2[::-1]
        for i in range(length):
            if i < len(s1):
                s3 = s3 + s1[i]
            if i < len(s2):
                s3 = s3 + s2[i]
        print(s3)

    # 7
    if (x == 7 or all is True):
        def test(s1, s2):
            check = True
            for i in s1:
                if not s2.__contains__(i):
                    check = False
                    print(s1+" and "+s2+" are not balanced")
                    return
            print(s1+" and "+s2+" are balanced")
        test("Yn", "PYnative")
        test("Ynf", "PYnative")

    # 8
    if (x == 8 or all is True):
        str1 = "Welcome to USA. usa awesome, isn't it? uSA"
        str2 = "usa"
        count = 0
        for i in range(len(str1)-2):
            if str1[i].lower() == "u":
                if str1[i+1].lower() == "s":
                    if str1[i+2].lower() == "a":
                        count = count + 1
        print("The "+str2+" count is "+str(count))

    # 9
    if (x == 9 or all is True):
        str1 = "PYnative29@#8496"
        count = 0; runtot = 0
        for i in str1:
            if i.isdigit():
                runtot += int(i)
                count = count + 1
        print("Sum is "+str(runtot)+". Average is "+str(runtot/count))

    # 10
    if (x == 10 or all is True):
        str1 = "Apple"
        dict = {}
        for i in str1:
            count = str1.count(i)
            dict[i] = count
        print(dict)

    # 11
    if (x == 11 or all is True):
        str1 = "PYnative"
        print(str1[::-1])

    # 12
    if (x == 12 or all is True):
        str1 = "Emma is a data scientist who knows Python. Emma works at google."
        print(str1.rindex("Emma"))

    # 13
    if (x == 13 or all is True):
        str1 = "Emma-is-a-data-scientist"
        print(str1.replace('-', '\n'))

    # 14
    if (x == 14 or all is True):
        str1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
        print(list(filter(None, str1)))

    # 15
    if (x == 15 or all is True):
        str1 = "/*Jon is @developer & musician"; str2 = ""
        str1 = re.sub(r'[^a-zA-Z\s]', '', str1)
        str1 = re.sub(r' +', ' ', str1)
        print(str1)

    # 16
    if (x == 16 or all is True):
        str1 = 'I am 25 years and 10 months old'
        str1 = re.sub(r'[\D]', '', str1)
        print(str1)

    # 17
    if (x == 17 or all is True):
        str1 = "Emma25 is Data scientist50 and AI Expert"
        elements = str1.split(sep=' ')
        alpha = [False if i.isalpha() else True for i in elements]
        print(list(compress(elements, alpha)))

    # 18
    if (x == 18 or all is True):
        str1 = '/*Jon is @developer & musician!!'
        str1 = re.sub(r'[^a-zA-Z\s]', '#', str1)
        print(str1)

print("Hello, welcome to the String Puzzle solutions.")
loop = True
while loop:
    x = input("\nPlease enter selection (1-18), 'all', or quit: ")
    if x == 'all':
        run(1,True)
    elif x[:1].lower() == 'q':
        break
    elif x.isdigit():
        run(int(x), False)
    else: loop = True
print("Goodbye!")
