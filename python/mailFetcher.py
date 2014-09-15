__author__ = 'Tyraan'
import poplib, pp13.mailconfig,sys

from .mailParser import MailParser
from .mailTool import MailTool,SilentMailTool


class DeleteSynchError(Exception):pass
class TopNotSupported(Exception):pass
class MessageSynchError(Exception):pass

class MailFetcher(MailTool):
    """
     fetch mail: connect,fetch headers+mails,delete mails,this subclass cache the implemented with
     the POP protocol;
     IMAP requires new class;
    """
    def __init__(self,popserver=pp13.mailconfig.popservername,popuser=pp13.mailconfig.popusername,poppswd=pp13.mailconfig.poppassword,hastop=True):
        self.popServer  = popserver
        self.popUser    = popuser
        self.srvrHasTop = hastop
        self.popPassword = poppswd

    def connect(self):
        self.trace('Connecting ...')
        self.getPassword()
        server = poplib.POP3(self.popServer)
        server.user(self.popUser)
        server.pass_(self.popPassword)
        self.trace(server.getwelcome())
        return server
    fetchEncoding = pp13.mailconfig.fetchEncoding
    def decodeFullText(self,messageBytes):

        text  =  None
        kinds = [self.fetchEncoding]
        kinds +=['gb18030','gbk','latin1','ascii']
        kinds +=[sys.getdefaultencoding()]
        for kind in kinds:
            try :
                text=[line.decode(kind) for line in messageBytes]
                break
            except(UnicodeError,LookupError):
                pass

        if text ==None:
            blankline = messageBytes.index(b'')
            hdrsonly  = messageBytes[:blankline]
            commons = ['ascii','latin1','utf8','gb18030','gbk']
            for common in commons:
                try:
                    text = [line.decode(common) for line in hdrsonly]
                    break
                except UnicodeError:
                    pass
            else:
                try:
                    text = [line.decode() for line in hdrsonly]
                except UnicodeError:
                    text = ['From :(sender of unknown Unicode format headers)']
            text +=['','--Sorry: mailtools cannot decode this mil content!--']
        return text


    def downloadMessage(self,msgnum):
        self.trace('load'+str(msgnum))
        server = self.connect()
        try:
            resp,msglines,respsz = server.retr(msgnum)
        finally:
            server.quit()
        msglines = self.decodeFullText(msglines)
        return '\n'.join(msglines)

    def downloadAllHeaders(self, progress=None, loadfrom =1):
        if not self.srvrHasTop:
            return self.downloadAllMsgs(progress,loadfrom)
        else:
            self.trace('loading headers ')
            fetchlimit = pp13.mailconfig.fetchlimit
            server = self.connect()
            try:
                resp,msginfos,respsz = server.list()
                msgCount = len(msginfos)
                msginfos = msginfos[loadfrom-1:]
                allsizes = [int(x.split()[1]) for x in msginfos]
                allhdrs = []
                for msgnum in range(loadfrom,msgCount+1):
                    if progress:progress(msgnum,msgCount)
                    if fetchlimit and (msgnum <= msgCount-fetchlimit):
                        hdrtext='Subject:--mail  skipped--\n\n'
                        allhdrs.append(hdrtext)
                    else:
                        resp,hdrlines,respsz = server.top(msgnum,0)
                        hdrlines = self.decodeFullText(hdrlines)
                        allhdrs.append('\n'.join(hdrlines))
            finally:
                server.quit()
            assert  len(allhdrs)==len(allsizes)
            self.trac('load headers exit')
            return allhdrs,allsizes,False

    def downloadAllMessages(self,progress=None,loadfrom=1):



    def deleteMessages(self):

    def deletemessageSafely(self):

    def checkSynchError(self):

    def headerMatch(self):
    def getPassword(self):



############################################################################################################
###special subclass
############################################################################################################
class MailFetcherConsole(MailFetcher):
    def askPopPassword(self):


class SilentMailFetcher(SilentMailTool,MailFetcher):
    pass
