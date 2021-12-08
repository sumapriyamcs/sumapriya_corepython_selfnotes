nums = [1, 2, 3, 4, 5, 6]

n = 2

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')


def print_sum_even_nums(even_nums):
    total = 0

    for x in even_nums:
        if x % 2 != 0:
            break

        total += x
    else:
        print("For loop executed normally")
        print(f'Sum of numbers {total}')


# this will print the sum
print_sum_even_nums([2, 4, 6, 8])

# this won't print the sum because of an odd number in the sequence
print_sum_even_nums([2, 4, 5, 8])

# Python program to demonstrate
# break statement

# Python program to
# demonstrate break statement

s = 'geeksforgeeks'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')

for i in range(4):
    for j in range(4):
        if j==2:
            break
        print("The number is ",i,j);

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100:
        break
    print('current number', i)

for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to break inner loop
        if i > 5 and j > 5:
            break
        print(i * j, end=' ')
    print('')
for i in range(1, 11):
    # condition to break outer loop
    if i > 5:
        break
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')

x = 0
for x in range(10):
    if x == 4:
        break
    print(x)


