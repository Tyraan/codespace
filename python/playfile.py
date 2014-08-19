__author__ = 'Tyraan'
import os,sys,mimetypes,webbrowser
helpmsg="""
This is a help message:
 Sorry ,script can't find a media player for %s on your system!
 Add an entry for your system to the media player directory for this type of file in playfile.py,or play the file manually.
 """

def trac(*args):print(*args)

class MediaTool:
    def __init__(self,runtext=''):
        self.runtext=runtext
    def run(self,mediafile,**options):
        fullpath=os.path.abspath(mediafile)
        self.open(fullpaht,**options)

class Fileter(MediaTool):
    def open(selfself,mediafile,**ignored):
        media = open(mediafile,'rb')
        player = os.popen(self.runtext,'w')
        player.write(media.read())

class Cmdline(MediaTool):
    def open(self,mediafile,**ignored):
        cmdline=self.runtext % mediafile
        os.system(cmdline)

class Winstart(MediaTool):
    def open(self,mediafile,wait=False,**other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT' +mediafile)

class Webbrowser(MediaTool):
    def open(self,mediafile,**options):
        webbrowser.open_new('file://%s '%mediafile,**options)



################################################################################################################################
#media- and platform-specific policies: change me ,or pass one in
################################################################################################################################
audiotools={
    'sunos5':Fileter('/usr/bin/audioplay'),
    'linux2':Cmdline('cat %s >/dev/audio'),
    'sunos4':Fileter('/usr/demo/SOUND/play'),
    'win32' :Winstart(),
   #'win32':Cmdline('start %s')
    }

videotools={
    'linux2':Cmdline('tkcVideo_c700 %s '),
     'win32':Winstart(),
    }


imagetools={
    'linux2':Cmdline('zimager %s'),
    'win32' : Winstart(),
    }

texttools = {
    'linux2':Cmdline('vi %s'),
    'win32' : Cmdline('notpad %s '),

    }

apptools={
    'win32': Winstart()

}

mimetable={
    'audio': audiotools,
    'video': videotools,
    'image': imagetools,
    'text' : texttools,
    'application':apptools,
}

############### top-level interfaces

def trywebbrowser(filename,helpmsg=helpmsg,**options):
    trac('trying brower',filename)
    try:
        player = Webbrowser()
        player.run(filename,**options)
    except:
        print(helpmsg % filename)



def playknownfile(filename,playertable={},**opntions):
    if sys.platform in playertable:
        playertable[sys.platform].run(filename,**opntions)
    else:
        trywebbrowser(filename,**opntions)


def playfile(filename,memetable=mimetable,**optons):
    contenttype,encoding=mimetypes.guess_type(filename)
    if contenttype==None or encoding is not None:
        contenttype='?/?'
    maintype,subtype=contenttype.split('/',1)
    if maintype=='text' and subtype =='html':
        trywebbrowser(filename,**options)
    elif maintype in mimetable:
        playknownfile(filename,mimetypes[maintype],**options)
    else:
        trywebbrowser(filename,**options)


###############################################################
####### self test code
###############################################################
if __name__=='__main__':
    playknownfile('sousa.au',audiotools,wait=True)
    playknownfile('ora-pp3e.gif',imagetools,wait=True)
    playknownfile('ora-lp4e.jpg',imagetools)

    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')
    playfile('ppriorcalendar.html')
    playfile('spam.doc')
    playfile('spreadsheet.xls')
    playfile('sousa.au',wait=True)
    input('Done')