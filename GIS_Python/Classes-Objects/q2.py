def myTest(a):
    if a ==[]:
        return a
    else:
        print 'MT=',myTest(a[1:])
        print 'a[0]=',[a[0]]
        return myTest(a[1:]) + [a[0]]
b = [2,5,6,8]

x = myTest(b)

print 'x=',x
