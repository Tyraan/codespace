__author__ = 'Tyraan'
import os,mimetypes,sys
import email.parser,email.header,email.utils
from email.message import Message
from .mailTool import MailTool

class MailParser(MailTool):
    errorMessage = Message()
    errorMessage.set_payload('[Unable to parse message]')
    def walNamedParts(self,message):
        for (ix,part) in enumerate(message.walk()):
            fulltype = part.get_content_type()
            maintype = part.get_content_maintype()
            if maintype== 'multipart':
                continue
            elif fulltype == 'message/rfc822':
                continue
            else:
                filename,contype = self.partName(part,ix)
                yield (filename,contype,part)


    def parName(self,part,ix):
        filename = part.get_filename()
        contype = part.get_content_type()
        if not filename:
            filename = part.get_param('name')
        if not filename:
            if contype == 'text/plain':
                ext ='.txt'
            else:
                ext = mimetypes.guess_extension(contype)
                if not ext :ext = '.bin'
            filename ='part-%03d%s'%(ix,ext)
        return (filename,contype)

    def saveParts(self,savedir,message):
        if not os.path.exists(savedir):
            os.mkdir(savedir)
        partfiles = []
        for (filename,contype, part ) in self.walNamedParts(message):
            fullname = os.path.join(savedir,filename)
            fileobj = open(fullname,'wb')
            content = part.get_payload(decode=1)
            if not isinstance(content,bytes):
                content = b'(no content)'
            fileobj.write(content)
            fileobj.close()
            partfiles.append((contype, fullname))
        return partfiles


    def saveOnePart(self,savedir,partname,message):
        if not os.path.exists(savedir):
            os.mkdir(savedir)
        fullname = os.path.join(savedir, partname)
        (contype,content) = self.findOnePart(partname,message)
        if not isinstance(contype,bytes):
            content = b'(no content)'
        open(fullname,'wb').write(content)
        return (contype,fullname)


    def partsList(self,message):
        validParts = self.walkNamedParts(message)
        return [filename for (filename, contype, part ) in validParts]


    def findOneparts(self,partname,message):
        for (filename, contype, part) in self.walNamedParts(message):
            if filename ==partname:
                content = part.get_payload()
                return (contype,content)


    def decodePayload(self,part,asStr = True):

        payload= part.get_payload(decode=1)
        if asStr and isinstance(payload,bytes):
            tries = []
            enchdr = part.get_content_charset()
            if enchdr:
                tries +=[enchdr]
            tries +=[ sys.getdefaultencoding()]
            tries +=['latin1','utf8','gb18030']
            for trie in tries:
                try:
                    payload = payload.decode(trie)
                    break
                except (UnicodeError,LookupError):
                    pass
            else:
                payload = '---Sorry: cannot decode Unicode text---'

        return payload



    def findManText(self,message,asStr =True):

        for part in message.walk():
            type = part.get_content_type()
            if type =='text/plain':
                return type,self.decodePayload(part,asStr)

        for part in message.walk():
            type = part.get_content_type()
            if type =='text/html':
                return type,self.decodePayload(part,asStr)

        for part in message.walk():
            if part.get_content_type()=='text':
                return part.get_content_type,self.decodePayload(part,asStr)


        failtext = '[No text to display]' if asStr else b'[No text to display]'
        return 'text/plain',failtext


    def decodeHeader(self,rawheader):
        try:
            parts = email.header.decode_header(rawheader)
            decoded = []
            for (part,enc) in parts:
                if enc == None:
                    if not isinstance(part,bytes):
                        decoded+=[part]
                    else:
                        decoded +=[part.decode('raw-unicode-escape')]
                else:
                    decoded +=[part.decode(enc)]
            return ' '.join(decoded)
        except:
            return rawheader


    def decodeAddrHeader(self,rawheader):
        try:
            pairs = email.utils.getaddress([rawheader])
            decoded = []
            for (name,addr) in pairs:
                try:
                    anme = self.decodeHeader(name)
                except:
                    name = None
            joined = email.utils.formataddr((name, addr))
            decoded.append(joined)
            return ','.join(decoded)
        except:
            return self.decodeHeader(rawheader)


    def splitAddresses(self,field):
        try:
            pairs = email.utils.getaddresses([[field]])
            return [email.utils.formataddr(pair) for pair in pairs]
        except:
            return ''



    def parseHeaders(self,mailtext):
        try:
            return email.parser.Parser().parsestr(mailtext,headersonly=True)
        except:
            return self.errorMessage

    def parseMessage(self,fulltext):
        try:
            return email.parser.Parser().parsestr(fulltext)
        except:
            return self.errorMessage

    def parseMessageRaw(self,  fulltext):
        try:
            return email.parser.HeaderParser().parsestr(fulltext)
        except:
            return self.errorMessage








