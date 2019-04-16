
print('\nHow to Copy or Rename a Matrix, List, in Python')

print('\nlist a and b=a then change a')
a = [3,4,5]
b = a
print("a and b:")
print(a,b)
a[0] = 2
print(a,b)

print('\nnew list a, b = a[:], change a ')
a = [3,4,5]
b = a[:]
print("a and b:")
print(a,b)
a[0] = 2
print(a,b)

print('\nnew list a, b = list(a), change a')
a = [3,4,5]
b = list(a)
print("a and b:")
print(a,b)
a[0] = 2
print(a,b)

print('\nnew list a, b = copy.a, change a')
a = [3,4,5]
b = a.copy()
print("a and b:")
print(a,b)
a[0] = 2
print(a,b)

input()

