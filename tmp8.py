a  = ((i,j) for i in range(3) for j in range(3))

for x,y in a:
    if y == 1:
        break
        print('x,y before next ',x,y)
        
        #print('next ',next(a))
        #print('x,y after next ',x,y)
    print('x and y: ',x,y)

