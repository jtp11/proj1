print(""" This prog. uses a generator expression
 with nested loops to make indices """)
input('input: ')
def pairs_range(limit1, limit2):
    """Produce all pairs in (0..`limit1`-1, 0..`limit2`-1)"""
    for i1 in range(limit1):
        for i2 in range(limit2):
            yield i1, i2

for x, y in pairs_range(3, 5):
    #if some_condition(x, y):
     #   break
    print('x and y: ',x, y)
input('input: ')    

print("""Double generator
pairs = ((i1, i2) for i1 in range(10) for i2 in range(20))
for x,y in pairs:
    print('x and y: ',x,y)
""")
      
pairs = ((i1, i2) for i1 in range(3) for i2 in range(5))
#for (i,j) in [(i,j) for i in range(x) for j in range(y)]
for x,y in pairs:
    #if some_condition(x, y):
    #    break
    print('x and y: ',x,y)

input('input: ')

print("""Double for loop
for (i,j) in [(i,j) for i in range(3) for j in range(6)]:
   print('x and y: ',i,j)
""")
for (i,j) in [(i,j) for i in range(3) for j in range(6)]:
   print('x and y: ',i,j)
input('input: ')
    
