from socket import *
import os
import struct
__author__= 'Tyraan'

ADDR = ('localhost',50007)
BUFSIZE = 1024

filename = '天龙八部.txt'
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

sendSock = socket(AF_INET,SOCK_STREAM)
sendSock.connect(ADDR)

fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
sendSock.send(fhead)

fp = open(filename,'rb')
while 1:
    filedata = fp.read(BUFSIZE)
    if not filedata: break
    sendSock.send(filedata)
fp.close()

sendSock.close()





