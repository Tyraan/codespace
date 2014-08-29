__author__ = 'Tyraan'

服务端：
#!/usr/bin/python
#coding:utf-8
import SocketServer
import subprocess
import string
import time
class MyTcpServer(SocketServer.BaseRequestHandler):
    def recvfile(self, filename):
        print("starting reve file!")
        f = open(filename, 'wb')
        self.request.send('ready')
        while True:
            data = self.request.recv(4096)
            if data == 'EOF':
                print("recv file success!")
                break
            f.write(data)
        f.close()

    def sendfile(self, filename):
        print "starting send file!"
        self.request.send('ready')
        time.sleep(1)
        f = open(filename, 'rb')
        while True:
            data = f.read(4096)
            if not data:
                break
            self.request.send(data)
        f.close()
        time.sleep(1)
        self.request.send('EOF')
        print "send file success!"

    def handle(self):
        print "get connection from :",self.client_address
        while True:
            try:
                data = self.request.recv(4096)
                print "get data:", data
                if not data:
                    print "break the connection!"
                    break
                else:
                    action, filename = data.split()
                    if action == "put":
                        self.recvfile(filename)
                    elif action == 'get':
                        self.sendfile(filename)
                    else:
                        print "get error!"
                        continue
            except Exception,e:
                print "get error at:",e


if __name__ == "__main__":
    host = ''
    port = 60000
    s = SocketServer.ThreadingTCPServer((host,port), MyTcpServer)
    s.serve_forever()


客户端：

import socket
import sys
import time
ip = '192.168.1.214'
port = 60000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def recvfile(filename):
    print "server ready, now client rece file~~"
    f = open(filename, 'wb')
    while True:
        data = s.recv(4096)
        if data == 'EOF':
            print "recv file success!"
            break
        f.write(data)
    f.close()
def sendfile(filename):
    print "server ready, now client sending file~~"
    f = open(filename, 'rb')
    while True:
        data = f.read(4096)
        if not data:
            break
        s.sendall(data)
    f.close()
    time.sleep(1)
    s.sendall('EOF')
    print "send file success!"

def confirm(s, client_command):
    s.send(client_command)
    data = s.recv(4096)
    if data == 'ready':
        return True

try:
    s.connect((ip,port))
    while 1:
        client_command = raw_input(">>")
        if not client_command:
            continue

        action, filename = client_command.split()
        if action == 'put':
            if confirm(s, client_command):
                sendfile(filename)
            else:
                print "server get error!"
        elif action == 'get':
            if confirm(s, client_command):
                recvfile(filename)
            else:
                print "server get error!"
        else:
            print "command error!"
except socket.error,e:
    print "get error as",e
finally:
    s.close()