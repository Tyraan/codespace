__author__ = 'Tyraan'
from tkinter import *
import sys
def quit1():
    print('quit !')
    quit()
wi=Button(None,{'text':'Hello widgte world'},command=(lambda :print('Here lambda function') or quit1() ))
wi.pack()
wi.mainloop()


wid=Button(None,text='Hello widget',command=sys.exit)
wid.pack()
wid.mainloop()

widg=Button(None,text='Event!',command=quit)

