__author__ = 'Tyraan'

import sys
def doSomething():
    if __name__=='__main__':
        args = sys.argv
        if args:print 'get a args ',args
        print 'been called!'


doSomething()




