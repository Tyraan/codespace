__author__ = 'Tyraan'

from tkinter import *
root=Tk()
trees=[('The Larch!','light blue'),
    ('the main','light yellow'),
    ('the Pine','red')]

for (t,c) in trees:
    win=Toplevel(root)
    win.title('sing the same song')
    win.protocol('WM_DELETE_WINDOW',lambda:None)


    msg = Button(win,text=t,command=win.destroy)
    msg.pack(expand=YES,fill=BOTH)
    msg.config(padx=10,pady=10,bd=10,relief=RAISED)
    msg.config(bg='black',fg=c,font=('times',30,'bold italic'))

root.title('Lumberjack demo')
Label(root,text='Main window',width=30).pack()
Button(root,text='Quit All',command=root.quit).pack()
root.mainloop()