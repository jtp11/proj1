print(
"""Simply speaking, a generator is a function that returns
an object (iterator) which we can iterate over (one value at a time).

Generator function 

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

"""
)
input()

print('\n Using a Generator Function, Reverse a String:\n')

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

for char in rev_str("hello"):
     print(char)
input()

print('\n Using a Generator Function, Calculate Prime Numbers:\n')

def check_prime(num):
  n = int(num**.5)+1
  for i in range(2 , n):
    if (num % i) == 0:
      return False
  return True

def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number

p = Primes(40)

print(list(Primes(40)))
print(list(p))

for x in p:
    print(x)
input()

      

#Generator Expression
print(
"""generator expressions don’t construct list objects.
Instead, they generate values “just in time” like a
class-based iterator or generator function would.

my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)
""")

# Intialize the list

my_list = [1, 3, 6, 10]
print(my_list)
a = (x**2 for x in my_list)

#Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))


print('\nUseing a Generator Expression, Print a List\n')

my_list = [1, 3, 6, 10]
#my_list = [1,3,6,10]
print('the list: ',my_list)

a = (x**2 for x in my_list)
print('\nPrint the value from the list which is the item squared\n',list(a))

print('\nPrint value in a where value is item squared.')
a = (x**2 for x in my_list)
for y in a:
  print(y)
input()

print('\nUseing a Generator Expression, Calculate Even Squares\n')

even_squares = (x * x for x in range(10) if x % 2 == 0)
for x in even_squares:
     print(x)
input()



