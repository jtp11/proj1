
print("""
COMPARE LIST COMPREHENSIONS TO GENERATOR EXPRESSIONS

generator expressions take less space than list comprehensions

import sys
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))

input() \n\n Results:\n """  )

import sys
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print('size of comprehension',sys.getsizeof(g))

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print('size of generator',sys.getsizeof(l))

input()

print( """
generator expressions can run slower than list comprehensions
unless you run out of memory, of course


import cProfile
cProfile.run \
('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')

cProfile.run \
('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')

Results:\n """)

import cProfile
cProfile.run \
    ('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')

cProfile.run \
    ('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')

input()

print("""
Use time() function to check on time to run statement.

y = sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))
Result:

""")



import time
t1 = time.time()
y = sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))
t2 = time.time()
print('time ',(t2-t1))

print("""\n
y = sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])
Result:

""")


t1 = time.time()
y = sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])
t2 = time.time()
print('time ',(t2-t1))

input()

