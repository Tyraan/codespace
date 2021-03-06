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
        self.trace('downloading full messages ')
        fetchlimit = pp13.mailconfig.fetchlimit
        server = self.connect()
        try:
            (msgCount,msgBytes) = server.stat()
            allmsgs  = []
            allsizes = []
            for i in range(loadfrom, msgCount+1):
                if progress:progress(i,msgCount)
                if fetchlimit and (i<=msgCount - fetchlimit):
                    mailtext = 'Subject :--mail skiped -- \n\nMail skipped.\n'
                    allmsgs.append(mailtext)
                    allsizes.append(len(mailtext))
                else:
                    (resp,message,respsz) = server.retr(i)
                    message = self.decodeFullText(message)
                    allmsgs.append('\n'.join(message))
                    allsizes.append(respsz)
        finally:
            server.quit()
        assert len(allmsgs)==(msgCount-loadfrom)+1
        return allmsgs,allsizes,True


    def deleteMessages(self,msgnums,progress=None):
        self.trace('deleting mails...')
        server = self.connect()
        try:
            for (ix, msgnum) in enumerate(msgnums):
                if progress:progress(ix+1,len(msgnums))
                server.dele(msgnum)
        finally:
            server.quit()









    def deletemessageSafely(self,msgnums,synchHeaders,progress=None):
        if not self.srvrHasTop:
            raise TopNotSupported('Safe delete cancelled.')
        self.trace('deleting mails safely')
        errmsg = 'Message %s out of synch with server.\n'
        errmsg +='Delete terminated at this message.\n'
        errmsg += 'Mail client may require restart or reload.'

        server = self.connect()
        try:
            (msgCount,msgBytes) = server.stat()
            for (ix,msgnum)in enumerate(msgnums):
                if progress:progress(ix+1,len(msgnums))
                if msgnum > msgCount:
                    raise DeleteSynchError(errmsg% msgnum)
                resp,hdrlines,respsz = server.top(msgnum, 0)
                hdrlines = self.decodeFullText(hdrlines)
                msghdrs = '\n'.join(hdrlines)

                if not self.headerMatch(msghdrs,synchHeaders[msgnum-1]):
                    raise DeleteSynchError(errmsg % msgnum)
                else:
                    server.dele(msgnum)
        finally:
            server.quit()




    def checkSynchError(self,synchHeaders):
        self.trace('synch check')
        errormsg = 'Message index out of synch with mail server.\n'
        errormsg +='Mail clien may require restart or reload.'
        sever = self.connect()
        try:
            lastmsgnum = len(synchHeaders)
            (msgCount,msgBytes) = server.stat()
            if lastmsgnum>msgCount:
                raise MessageSynchError(errormsg)
            if self.srvrHasTop:
                resp,hdrlines,respz = server.top(lastmsgnum,0)
                hdrlines = self.decodeFullText(hdrlines)
                lastmsghdrs = '\n'.join(hdrlines)
                if not self.headerMatch(lastmsghdrs,synchHeaders[-1]):
                    raise MessageSynchError(errormsg)
        finally:
            server.quit()



    def headerMatch(self,hdrtext1,hdrtext2):
        if hdrtext1==hdrtext2:
            return True
        split1 = hdrtext1.splitlines()
        split2 = hdrtext2.splitlines()
        strip1 = [line for line in split1 if not line.startswith('Status:')]
        strip2 = [line for line in split2 if not line.startswith('Status:')]
        if strip1==strip2:
            self.trace('same without status.')
            return True
        msgid1 = [line for line in split1 if line[:11].lower()=='message-id:']
        msgid2 = [line for line in split2 if line[:11].lower()=='message-id:']
        if (msgid1 or msgid2) and (msgid1 != msgid2):
            self.trace('different message id ')

            return False
        tryheaders = ('From','To','Subject','Date')
        tryheaders+=( 'Cc','Return-Path','Received')
        msg1 = MailParser().parserHeaders(hdrtext1)
        msg2 = MailParser().parserHeaders(hdrtext2)
        for hdr in tryheaders:
            if msg1.get_all(hdr) != msg2.get_all(hdr):
                self.trace('Different common headers ')
                return False
        self.trace('Same common headers')
        return True


    def getPassword(self):

        if not self.popPassword:
            try:
                localfile = open('pp13.mailconfig.poppasswdfile')
                self.popPassword = localfile.readline()[:-1]
                self.trace('localfile password'+ repr(self.popPassword))

            except:
                self.popPassword = self.askPopPassword()

    def askPopPassword(self):
        assert False,'subclass must  define method for askPopPassword'








############################################################################################################
###special subclass
############################################################################################################
class MailFetcherConsole(MailFetcher):
    def askPopPassword(self):
        import getpass
        promt = 'Password for %s on %s'%(self.popUser,self.popServer)
        return getpass.getpass(promt)



class SilentMailFetcher(SilentMailTool,MailFetcher):
    pass
