__author__ = 'Tyraan'
import sys,os,multiprocessing

import big_tree
from stream_redirection import *


def server1():
    mypid = os.getpid()
    conn  = initListenerSocket()
    file  = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print('server %s got [%s]'%(mypid, data))

def client1():
    mypid=os.getpid()
    redirectOut()
    for i in range(3):
        print ('client) %s: %s'%(mypid, i))
        sys.stdout.flush()



def server2():
    mypid = os.getpid()
    conn = initListenerSocket()
    for i in range(3):
        data = input()
        print('Client %s got [%s]'%(mypdi, data))

def client2():
    mypid=os.getpid()
    redirectIn()
    for i in range(3):
        data = input()
        print('client %s got [%s]'%(mypid, data))



def server3():
    mypid=os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        conn.send(('server %s got [%s]\n'%(mypid,data)).encode())

def client3():
    mypid = os.getpid()
    redirectBothAsClient()
    for i in range(3):
        print('client %s %s '%(mypid,i))
        data = input(())
        sys.stderr.write('client %s got [%s ]'%(mypid, data ))



def server4():
    mypid = os.getpid()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host,port))
    file = sock.makefile('r')
    for i in range(3):
        sock.send(('server 4 %s :%s \n'%(mypid, i)))

        data = file.readline().rstrip()
        print ('server %s got [%s'%(mypid, data))

def client4():
    mypid=os.getpid()
    redirectBothAsServer()
    for i in range(3):
        data = inpu()
        print ('client %s got [%s'%(mypid, data))
        sys.stdout.flush()



def server5():
    mypid = os.getpid()
    conn  = initListenerSocket()
    file  = conn.makefile('r')
    for i in range(3):
        conn.send(('server %s : %s \n'%(mypid, i)).encode())
        data = file.readline().rstrip()
        print ('server %s got [%s]'%(mypid,data))

def client5():
    mypid = os.getpid()
    s= recirectBothAsClient()
    for i in range(3):
        data = input()
        print ('client %s got [%s'%(mypid, data))
        sys.stdout.flush()


##################################################################################
#test code                                                      ##################
##################################################################################
if __name__=='__main__':
    server = eval('server'+ sys.argv[1])
    client = eval('client'+ sys.argv[1])
    multiprocessing.Process(target=server).start()
    client
    #import time;time.sleep(5)
