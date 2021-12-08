print("--------For loop with String-------")
msg = 'Hello World'

for char in msg:
    print("Character : ", char)

for element in msg:
    print("Character : ", element)

#Write a program to display the largest word from the string:?
str=input("Enter any String :")
L = str.split()
max=0
b=""
for i in L:
     if len(i) > max:
           b=i
           max=len(i)
print("Longest word is ",b)

#Write a program to accept a string and display the ascii value of each character.?

str=input("Enter any String :")
for i in str:
     print("ASCII value of ",i,"is",ord(i))

#Write a program to accept a string and replace all spaces by ‘#’ symbol.?
str=input("Enter any String :")
str1=""
for i in str:
      if i.isspace():
          str1=str1+'#'
      else:
          str1=str1+i
print("Output String is :",str1)

#Write a program to accept two strings from the user and display the common words.(Ignore case)?

str1=input("Enter first String :")
str2=input("Enter second String :")
L1=str1.split()
L2=str2.split()
for i in L1:
     if i in L2:
         print(i)
# Write a program to display the smallest word from the string.?

str=input("Enter any String :")
L = str.split()
min=50 #we think that length of any word in the string is not larger than 50 (can give any other number)
b=""
for i in L:
     if len(i) < min:
           b=i
           min=len(i)
print("Smallest word is : ",b)

# write a program count how many times particular character will repeat in string:?
# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

s = "protagonist"
for index in range(0, len(s)):
    print(s[index])

#write a program  to reverse a string

s = input("Enter a string: ")
rev = ""
for i in range(len(s)-1, -1, -1):
   rev = rev + s[i]
print("The reverse of the string is: %s." % rev)



s = input("Enter a string: ")
rev = ""
for index in range(0, len(s)):
    rev = s[index] + rev
print("The reverse of the string is: %s." % rev)

s = input("Enter a string: ")
rev = ""
for ch in s:
   rev = ch + rev
print("The reverse of the string is: %s." % rev)

#find the index of a space in a string:?
fullname = input("Enter your full name: ")
for index in range(0, len(fullname)):
    if fullname[index] == ' ':
         space = index
         break

firstname = fullname[0:space]
print("Your first name is %s." % firstname)

'''3 Write a Python program to count the number of characters (character frequency) in a string?'''
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

# Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

#Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))








