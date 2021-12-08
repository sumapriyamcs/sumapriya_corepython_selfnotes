nums = [1, 2, -3, 4, -5, 6]

sum_positives = 0

for num in nums:
    if num < 0:
        continue
    sum_positives += num

print(f'Sum of Positive Numbers: {sum_positives}')

# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

for i in range(10):
    if i == 7:
        continue
    print("The Number is :" , i)

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
#continue statement in for loop
numbers = [2, 3, 11, 7]
for i in numbers:
    print('Current Number is', i)
    # skip below statement if number is greater than 10
    if i > 10:
        continue
    square = i * i
    print('Square of a current number is', square)
#Continue Statement in Nested Loop:?
for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to skip current iteration
        if j == 5:
            continue
        print(i * j, end=' ')
    print('')

#Continue Statement in Outer loop:?

for i in range(1, 11):
    # condition to skip iteration
    # Don't print multiplication table of even numbers
    if i % 2 == 0:
        continue
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')

x = 0
for x in range(10):
    if x == 4:
        continue
    print(x)



