__author__ = 'Tyraan'
import sys

def readers(F):
    tmp,sys.stdin =sys.stdin,F
    line= input()
    print (line)
    sys.stdin =tmp

readers (open('test-stream-modes.py'))
readers (open('test-stream-modes.py','rb'))
def writer(F):
    tmp,sys.stdout = sys.stdout, F
    print (99,'spam')
    sys.stdout = tmp


writer( open ('temp','w'))
print(open('temp').read())

writer(open('temp','wb'))
writer(open('temp','w',0 ))
