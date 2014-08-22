__author__ = 'Tyraan'
import time
from socket import *
sock=socket()
sock.connect(('localhost',6000))
file = sock.makefile('w',buffering=1)

print ('sending data1')
file.write('this is data1: SPAM')
time.sleep(5)
file.flush()

print ('sending data2 ')
print ('This is data 2:EGGS',file=file)
time.sleep(5)
file.flush()

print ('sending data3')
sock.send(b'this is data3 : HAM')
time.sleep(5)