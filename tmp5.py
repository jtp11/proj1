print('Test of rstrip().  There is a lstrip() also')
print('How to print without the end space')
print()
string2 = r'This is Test String to strip trailing space    '
print (string2,'xxx')
print (string2.rstrip().lstrip(),'xxx')
print (string2.rstrip(),end = '')
print ('xxx')
input()
