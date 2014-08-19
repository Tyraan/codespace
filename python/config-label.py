__author__ = 'Tyraan'


class ConfigLabel:
    def __init__(self):
        self.name='ConfigLable'
        root=Tk()
        labelfont=('times',20,'bold')
        widget=Label(root,text='Hello config ')
        widget.config(height=3,width=20,font=labelfont,bg='black',fg='yellow')
        widget.pack(expand=YES,fill=BOTH)
        root.mainloop()
    def quit(self):
        print('%s quit'%(self.name,))
        sys.exit()
class ConfigButton:
    def __init__(self):
        self.name='ConfigButton'
        widget=Button(text=self.name,padx=10,pady=10)
        widget.pack(padx=20,pady=20)
        widget.config(cursor='gumby',bd=8,relief=RAISED,bg='dark green',fg='white',font=('helvetica',20,'underline italic'))
        mainloop()




class TopLevel:
    def __init__(self):
        self.name='TopLevel'

        win=Toplevel()
        Button(win,text=self.name,command=sys.exit).pack()
        Label(text= 'Lable' ).pack() #寻找失散多年的孙子，特征：秒退我主机。
        win.mainloop()



if __name__=='__main__':
    import tkinter
    from tkinter import  Tk,Button
    tkinter.NoDefaultRoot()
    w1=Tk()
    w2=Tk()
    Button(w1,text='somthing',command=w1.destroy).pack()
    Button(w2,text='Other something' ,command=w2.destroy).pack()
    w1.mainloop()
