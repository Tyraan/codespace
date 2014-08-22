__author__ = 'Tyraan'
from socket import *
sock=socket()
sock.bind(('',6000))
sock.listen(5)
print ('accepting... ')
conn, id = sock.accept()

for i in range(3):
    print ('receiving ')
    print ( conn.recv(1024))

