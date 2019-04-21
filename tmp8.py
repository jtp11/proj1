print('testing \'next\' to break on y value, skips next item instead')
print('using \'continue\' on each trial of the inner loop')
print('will skip the rest of the loop')
print('break will leave both loops')

a  = ((i,j) for i in range(5) for j in range(5))

for x,y in a:
    if y >= 2 and x == 2: #pass
        continue
        #print('x,y before next ',x,y)
        #next(a)
        #print('next           ',next(a))
        #print('x,y after  next ',x,y)
    if y == 3 and x == 3: break
    print('x and y: ',x,y)
input()
