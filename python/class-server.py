__author__ = 'Tyraan'
import socketserver,time
myHost=''
myPort=50007

def now():
    return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address,now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data:break
            reply = 'this is reply %s at %s'%(data,now())
            self.request.send(reply.encode())
        self.request.close()

socketserver.ThreadingTCPServer((myHost,myPort),MyClientHandler).serve_forever()
