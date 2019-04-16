print('Print 3 lists in a with for:')
print('''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()''')

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

print('''\nBut the easiest way is to use generator,
      creating a list of n elements, each of which
      is a list of m zeros:
n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)

a = [0] * 3
for i in range(len(a)):
    a[i] = i
print(a)

n = 5
a = [0] * n
print(a)
input()
''')

n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)

a = [0] * 3
for i in range(len(a)):
    a[i] = i
print(a)


n = 5
a = [0] * n
print(a)
input()


print('''Generators

#[expression for variable in sequence]
a = [0 for i in range(5)]
print(a)
n = 5
a = [i ** 2 for i in range(n)]
print(a)
input()
''')



#[expression for variable in sequence]
a = [0 for i in range(5)]
print(a)
n = 5
a = [i ** 2 for i in range(n)]
print(a)
input()

'''
Comprehensions

A comprehension is roughly speaking just an expression that specifies a sequence of values - think of it as a compact for loop. In Python a comprehension can be used to generate a list.

This means that we can use a comprehension to initialize a list so that it has a predefined size. The simplest form of a list comprehension is

[expression for variable in list]

For example, to create the list equivalent of a ten-element array you could write:

myList=[0 for i in range(10)]




def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci

(5)
for x in f:
    print(x, " ", end="") # 
print()


>>> from sys import getsizeof
>>> my_comp = [x * 5 for x in range(1000)]
>>> my_gen = (x * 5 for x in range(1000))
>>> getsizeof(my_comp)
9024  
>>> getsizeof(my_gen)
88


Generator Expressions

Just like list comprehensions, generators can also be written in the same manner except they return a generator object rather than a list:

>>> my_list = ['a', 'b', 'c', 'd']
>>> gen_obj = (x for x in my_list)
>>> for val in gen_obj:
...     print(val)

>>> def countdown(num):
...     print('Starting')
...     while num > 0:
...         yield num
...         num -= 1
...
>>> val = countdown(5)
>>> val
<generator object countdown at 0x10213aee8>


Generator objects execute when next() is called:

>>> next(val)
Starting
5


>>> next(val)
4
>>> next(val)
3
>>> next(val)
2
>>> next(val)
1
>>> next(val)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


Generator Expressions

Just like list comprehensions, generators can also be written in the same manner except they return a generator object rather than a list:

>>> my_list = ['a', 'b', 'c', 'd']
>>> gen_obj = (x for x in my_list)
>>> for val in gen_obj:
...     print(val)
...
a
b
c
d

Be careful not to mix up the syntax of a list comprehension with a generator expression - [] vs () - since generator expressions can run slower than list comprehensions (unless you run out of memory, of course):

>>> import cProfile
>>> cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')
         4666672 function calls in 3.531 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  4666668    2.936    0.000    2.936    0.000 <string>:1(<genexpr>)
        1    0.001    0.001    3.529    3.529 <string>:1(<module>)
        1    0.002    0.002    3.531    3.531 {built-in method exec}
        1    0.592    0.592    3.528    3.528 {built-in method sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')
         5 function calls in 3.054 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.725    2.725    2.725    2.725 <string>:1(<listcomp>)
        1    0.078    0.078    3.054    3.054 <string>:1(<module>)
        1    0.000    0.000    3.054    3.054 {built-in method exec}
        1    0.251    0.251    0.251    0.251 {built-in method sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

This is particularly easy (even for senior developers) to do in the above example since both output the exact same thing in the end.

    NOTE: Keep in mind that generator expressions are drastically faster when the size of your data is larger than the available memory.


'''

