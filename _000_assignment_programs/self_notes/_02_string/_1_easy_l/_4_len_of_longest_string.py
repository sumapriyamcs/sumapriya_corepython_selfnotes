"""
4. write a program to get the length of the longest string ?

  I. CRUD            :  Retrieve
 II. State(variable) :  Datatype/strcuture   str = 'mcs is a best platform to learn new things'
III. Behavior        :  (Operators,DM,Loops)  =,>   for/while

#0 mathematics:
take a string from the user to perform operation
split that string and take a one key to store length of the word and applying
max function to get the longest word and store all these in one variable.
print that variable to get the longest word and use len function for that variable to get the length.

# 1: by using inbuilt functions

# Longest word

# Reading sentence from user

sentence = input("Enter sentence: ")

# Finding longest word
longest = max(sentence.split(), key=len)

# Displaying longest word
print("Longest word is: ", longest)
print("And its length is: ", len(longest))

#2. algorithm:
def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
          print(word, len(word))


words = input('Please enter a few words')
word_list = words.split()
find_longest_word(word_list)

#3. by using functions:

def longestWordLength(string):
    length = 0   # Initilize length to 0
    w = ''       # Initlize word to empty

    # Finding longest word in the given sentence and word
    for word in string.split():
        if(len(word) > length):
            length = len(word)
            w = word
    return (length, w)

string = input("Enter the string: ")
l, w = longestWordLength(string)
print("Longest word is ", w, " and its length is ", l)

# 4: by using oops:

class string:

    def __init__(self,longest,len):
        self.longest=longest
        self.len=len
    def getstrinfo(self):
        print("the longest string and length is",self.longest,self.len)
str1=string("morning",6)
str1.getstrinfo()


"""