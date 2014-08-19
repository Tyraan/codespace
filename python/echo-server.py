__author__ = 'Tyraan'
"""opent a tcp/ip on a port ,listen for a message from client side,and send an echo reply;"""
from socket import *
myHost=''
myPort = 50007
sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((myHost,myPort))
sockobj.listen()
while True:
    connection,address =sockobj.accept()
    