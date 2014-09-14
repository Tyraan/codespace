__author__ = 'Tyraan'
import poplib,smtplib,email.utils,mailconfig
from email.parser import Parser
from email.message import Message

fetchEncoding = mailconfig.fetchEncoding

helptext = """
  availabel commands :
  index      - display all messages
  message n? - list all messages or just message n
  delete  n? - deleteall messages or just message n
  send       - compose and send a mail.
  save    n? - save all messages or just message n to a file
  quit       - quit pymail

"""



def decodeToUnicode(messageBytes,fetchEncoding=fetchEncoding):
    decodeList=[]
    for i in messageBytes:
        try:
            decodeList.append(i.decode(fetchEncoding))
        except UnicodeDecodeError:
            decodeList.append(i.decode('GBK'))

    return decodeList

def splitaddrs(field):
    pairs = email.utils.getaddresses([field])
    return [email.utils.formataddr(pair) for pair in pairs]

def inputmessage():
    import sys
    From = input('from ?').strip()
    To   = input('to   ?').strip()
    To   = splitaddrs(To)

    Subj = input('Subj ?').strip()

    print('Type message text,end with line = "."')
    text = ''
    while True:
        line = sys.stdin.readline()
        if line =='.\n':break
        text+=line
    return From,To,Subj,text


def sendmessage():
    From,To,Subj,text = inputmessage()
    msg = Message()
    msg['From']   = From
    msg['To']     = To
    msg['Subject']= Subj
    msg['Date']   = email.utils.formatdate(timeval=None, localtime=False, usegmt=False)
    msg.set_payload(text)

    server =smtplib.SMTP(mailconfig.smtpservername,587)
    server.ehlo()
    server.starttls()
    server.login(mailconfig.gmailaddr,mailconfig.gmailpssword)
    failed = server.sendmail(From,To,text)


def connect(servername,user,passwd):
    print('Connecting....')
    server = poplib.POP3(servername)
    server.user(user)
    server.pass_(passwd)

    print(server.getwelcome())
    return server

def loadmessages(servername,user,passwd,loadfrom=1):
    server = connect(servername,user,passwd)
    try:
        print(server.list())
        (msgCount,msgBytes) = server.stat()
        print('There are ',msgCount,'mail messgaes in ',msgBytes,'bytes')

        print('Retriving...')

        msgList = []
        for i in range(loadfrom, msgCount+1):
            (hdr,message,octets)= server.retr(i)
            message = decodeToUnicode(message)

            msgList.append('\n'.join(message))

    finally:
        server.quit()
    assert len(msgList)==(msgCount-loadfrom)+1

    return msgList


def deletemessages(servername,user,passwd,toDelete,verify=True):
    print ('To be deleted:',toDelete)
    if verify and input('Delete ??')[:1] not in ['y','Y']:
        print('Cancelled')
    else:
        server = connect (servername,user,passwd)
        try:
            print('Deleteing messages from server...')
            for msgnum in toDelete:
                server.dele(msgnum)

        finally:
            server.quit()


def showindex(msgList):
    count = 0
    for msgtext in msgList:
        msghdrs = Parser().parsestr(msgtext,headersonly =True)
        count +=1
        print('%d :\t%d bytes '%(count,len(msgtext)))
        for hdr in ('From','To','Date','Subject'):
            try:
                print('\t% -8s =>%s'%(hdr,msghdrs[hdr]))
            except KeyError:
                print('\t%-8s =>'%hdr)
        if count %5 ==0:
            input('[Press Enter key]')


def showmessage(i,msgList):
    if 1<=i<=len(msgList):
        print('-'*80 )
        msg = Parser().parsestr(msgList[i-1])

        content = msg.get_payload()
        if isinstance(content,str):
            content = content.rstrip()+'\n'
        print(content)
        print('-'*80)
    else:
        print('invalid message number')



def savemessage(i,mailfile,msgList):
    if 1 <=i <= len(msgList):
        savefile = open(mailfile,'a',encoding = mailconfig.fetchEncoding)
        savefile.write('\n'+msgList[i-1]+'-'*80+'\n')
    else:print('invalid message number')



def msgnum(command):
    try:
        return int(command.split()[-1])
    except:
        return -1




def interact(msgList,mailfile):
    showindex(msgList)
    toDelete=[]
    while True:
        try:
            command = input('[pymail] action ?(index,message,delete,send,save,quit,?)')
        except EOFError:
            command = 'quit'
        if not command:command = '*'

        if command =='quit':break

        elif command=='index':
            showindex(msgList)
        elif command=='message':
            if len(command) == 1:
                for i in range(1,len(msgList)+1):
                    showmessage(i,msgList)
            else:
                showmessage(msgnum(command),msgList)
        elif command=='save':
            if len(command) == 1:
                for i in range(1,len(msgList)+1):
                    savemessage(i,msgList)
            else:
                savemessage(msgnum(command),mailfile,msgList)
        elif command=='delete':
            if len(command)==1:
                toDelete = list(range(1,len(msgList)+1))
            else:
                delnum = msgnum(command)
                if (1<=delnum<=len(msgList)) and (delnum not in toDelete):
                    toDelete.append(delnum)
                else:print('invalide msg number')

        elif command=='send':
            sendmessage()
            #execfile('smtpmail.py,{})

        elif command=='?':
            print(helptext)

        else:
            print('more infomation : type "?" for command help')

    return toDelete




#testcode
print('before test code')
if __name__=='__main__':
    print(__name__)
    import getpass
    print('import getpass ,mailconfig')

    mailserver = mailconfig.popservername

    mailuser   = mailconfig.popusername

    mailfile   = mailconfig.savemailfile
    print ('mailserver  mailuser mailfile settled')
    mailpswd   = mailconfig.poppassword

    print ('Pymail email client')

    msgList    = loadmessages(mailserver,mailuser,mailpswd)
    toDelete   = interact(msgList,mailfile)
    if toDelete:deletemessages(mailserver,mailuser,mailpswd,toDelete)
    print('see ya')






        

