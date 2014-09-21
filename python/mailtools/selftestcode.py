__author__ = 'Tyraan'
import sys
sys.path.append('..')
import pp13.mailconfig as mailconfig

print('congif:',mailconfig.__file__)

from mailtools import (MailFetcherConsole,
                        MailSender,MailSenderAuthConsole,MailParser)


if not mailconfig.smtpuser:
    sender = MailSender(tracesize = 5000)
else:
    sender = MailSenderAuthConsole(tracesize = 5000)

sender.sendMessage(From  = mailconfig.myaddress,
                   To    = [mailconfig.myaddress],
                   Subj  = 'testing mailtools package',
                   extrahdrs = [('X-Mailer',  'mailtools')],
                   bodytext = ' this is my source code \n',
                    attaches = ['selftest.py'])



fetcher = MailFetcherConsole()


def status(*args):
    print(args)


hdrs ,sizes ,loadedall = fetcher.downloadAllHeaders(status)


for num, hdr in enumerate(hdrs[:5]):
    print(hdr)



if input ('load mail? ') in ('y','Y'):
    print(fetcher.downloadMessage(num+1).rstrip(),'\n','-'*70)

last5 = len(hdr) -4

msgs, sizes, loadedall = fetcher.downloadMessage(status, loadfrom=last5)
for msg in msgs:
    print(msg[:200],'\n','_'*70)

parser = MailParser()
for i in [0]:
    fulltext = msgs[i]
    message  = parser.parseMessage(fulltext)
    ctype,maintext = parser.findMainText(message)
    print('Parsed :',message['Subject'])
    print(maintext)

input('Presss anything to exit')


