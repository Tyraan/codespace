__author__ = 'Tyraan'
from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Verify','Do you really want to quit?'):
        showwarning('Yes','Quit not yet implemented')
    else:
        showinfo('No','Quit has been cancelled!')

errmsg='Sorry ,this is error msg.'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam',command=(lambda:showerror('spam',errmsg))).pack(fill=X)
mainloop()


