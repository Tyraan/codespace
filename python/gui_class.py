__author__ = 'Tyraan'
import sys
form tkinter import *
class Hello:
    def __init__(self):
        widget1=Button(None,text='Hello world!!',command=self.quit)
        self.name='Button of Hello class'

    def quit(self):
        print('This % has quit'%(self.name))
        sys.exit()


class HelloCallable(Hello):
    def __init__(self):
        super().__init__()
        self.name='Callable of HelloCallable class'

    def __call__(self):
        self.quit()

class DoubleButton(HelloCallable):
    def __init__(self):
        self.name='Double of DoubleButton class '
        super().__init()

class HelloExtender(Hello):
    def __init__(self)
        self.name='Extender of HelloExtender class'
    def make_widgets(self):
        Hello.make_widgets(self)
        Button(self,text='Extentd',command=self.quit).pack(side=RIGHT)

    def massage(self):
        print('hello',self.data)

class HelloPackage:
    def __init__(self,parent=None):
        self.top=Frame(parent)
        self.top.pack()
        self.data=0
        self.make_widgets()

    def make_widgets(self):
        Button(self.top,text='Bye',command=self.top.quit).pack(side=LEFT)
        Button(self.top,text='Hi',command=self.message).pack(side=LEFT)


    def message(self):
        self.data+=1
        print ("Hello,here is message %d"(self.data,))

