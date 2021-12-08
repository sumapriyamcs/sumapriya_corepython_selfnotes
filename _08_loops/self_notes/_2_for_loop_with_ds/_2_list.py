degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print ('list element:', C)
print ('The degrees list has', len(degrees), 'elements')

list = ["John", "David", "James", "Jonathan"]
for i in list:
    # The i variable will iterate over the elements of the List and contains each element in each iteration.
    print(i)

#add the elemets in the list
#Declaring the empty list
l =[]
#Number of elements will be entered by the user
n = int(input("Enter the number of elements in the list:"))
# for loop to take the input
for i in range(0,n):
    # The input is taken from the user and added to the list as the item
    l.append(input("Enter the item:"))
print("printing the list items..")
# traversal loop to print the list items
for i in l:
    print(i, end = "  ")

#delete the elements from the list
list = [0,1,2,3,4]
print("printing original list: ");
for i in list:
    print(i,end=" ")
list.remove(2)
print("\nprinting the list after the removal of first element...")
for i in list:
    print(i,end=" ")

#Write the program to remove the duplicate element of the list.

list1 = [1,2,2,3,55,98,65,65,13,29]
# Declare an empty list that will store unique values
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#Write a program to find the sum of the element in the list.

list1 = [3,4,5,9,10,12,24]
sum = 0
for i in list1:
    sum = sum+i
print("The sum is:",sum)

# Write the program to find the lists consist of at least one common element.

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,2,10]
for x in list1:
    for y in list2:
        if x == y:
            print("The common element is:",x)

lst = [10, 50, 75, 83, 98, 84, 32]

for x in lst:
    print(x)

#write a program to square the odd values present in the list:?
# for understanding, above generation is same as,
odd_square = []

for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x**2)

print (odd_square)
#Write a Python program to sum all the items in a list:?
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

#Write a Python program to multiply all the items in a list.:?
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))

#Write a Python program to get the largest number from a list.:?
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

#Write a Python program to get the smallest number from a list.?
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))

#Write a Python program to check a list is empty or not:?
l = []
if not l:
    print("List is empty")

# Write a Python program to print the numbers of a specified list after removing even numbers from it.:?
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)
#Write a Python program to get the difference between the two lists?
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

#Write a Python program to convert a list of characters into a string?
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)
#Write a Python program to find the index of an item in a specified list?
num =[10, 30, 4, -6]
print(num.index(30))




