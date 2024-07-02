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
