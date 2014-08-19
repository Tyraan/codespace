__author__ = 'Tyraan'
from tkinter import *
from tkinter.messagebox import askokcancel,showerror,askquestion
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat
from tkinter.filedialog import askopenfilename
from tkinter.dialog import Dialog
class Quitter(Frame):
    def __init__(self,parent=None):
        self.name='Quitter'
        Frame.__init__(self,parent)
        self.pack()
        widget=Button(self,text=self.name,command=self.quit)
        widget.pack(side=LEFT,expand=YES,fill=BOTH)
    def quit(self):
        ans=askokcancel('Verify exit',"Really quit?")
        if ans:Frame.quit()

class Demo(Frame):
    number=0
    demos ={'Open': askopenfilename,
            'Color': askcolor,
            'Query': lambda : askquestion('Warning','Youtyped"rm*\n Confirm ?'),
            'Error': lambda : showerror('Error!','Here is an error'),
            'Input': lambda : askfloat('Entry','Enter credit card number')
    }
    def __init__(self,parent=None,**option):
        Demo.number+=1
        self.name='Demo Frame'+str (Demo.number)
        Frame.__init__(self,parent,**option)
        self.pack()
        Label(self,text='').pack()
        for (key,value)in Demo.demos.items():
            Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
        Quitter(self).pack(side=TOP,fill=BOTH)

class OldDialogDemo(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        Pack.config(self)
        Button(self,text='Pop 1 of ',command=self.dialog1).pack()
        Button(self,text='Pop 2 of ',command=self.dialog2).pack()
    def dialog1(self):
        ans=Dialog(self,
                   title = 'Popup fun!',
                   text = 'example of fukcing stupid dialog!',
                   bitmap='questhead',
                   default= 0,
                   strings=('Yes','No','Cancel'))

        if ans.num==0:self.dialog2()

    def dialog2(self):
        Dialog(self,
               title = 'fuck!!',
               text = ' the ans.num is 0 ,how did you do ',
               bitmap='hourglass',
               default = 0,
               strings=('Fuck this !','Fuck that!'))

if __name__=='__main__':OldDialogDemo().mainloop()
