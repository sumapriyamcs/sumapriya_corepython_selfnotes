squares = {i: i * i for i in range(10)}
print(squares)

quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

primes = {x for x in range(2, 101) if all(x%y for y in range(2, min(x, 11)))}
print(primes)


class Person:

    def __init__(self, id, name, age, city):
        self.id = id
        self.name = name
        self.age = age
        self.city = city


persons = [Person(1, "Fred", 26, "San Francisco"),
           Person(2, "Ria", 31, "San Francisco"),
           Person(3, "Sayid", 23, "New York City")]

unique_cities = {person.city for person in persons}

print(unique_cities)

a={i for i in range(15)}
print(a)

a={i for i in range(20) if i%2==0}
print(a)

a ={i*i for i in range(5)}
print(a)

new_set=set()
for i in range(10):
    if(i%2==0):
        new_set.add(i)
print(new_set)

set={(i,j) for j in range(5,9) for i in range(8,12)}
print(set)
print(type(set))

# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
							set_using_comp)
