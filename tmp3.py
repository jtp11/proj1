# Calculates prime numbers
print('A correct algorithm for calculating prime numbers')
print()
rng =50
k = int(rng**.5)
#print('  ',k)
for i in range(2,rng):
  #print('i ',i)
  for j in range(2 , i):
    #print(' j ',j)
    if (i % j) == 0:
      break
  else:
    print('ans:  ' ,i)
input()    

    
