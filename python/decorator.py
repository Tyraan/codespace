def deco(f,*args):
    print('this is deco ')
    def indeco():
        print ('this is indeco scope')
        f(args)
        
    print ('this is after f called in deco')
    
    return indeco


@deco
def otherfunc(s):
    print('this is other function')
    print ('you input',s)



def deco1(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco
 
@deco1
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b
 
myfunc(1, 2)
myfunc(3, 4)
    
