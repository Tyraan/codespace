__author__ = 'Tyraan'
import smtplib,sys,email.utils,mailconfig
mailserver = mailconfig.smtpservername

From =
To   =
subj = "hello , this is python script used to send a mail to you qq mailbox" \
       "do u reecive this message ?"
Date = email.utils.formatdate()


text = ('From :%s \n To : %s\n Date: %s\nSubject: %s\n\n'%(From,To,Date,subj))


print ('Connecting 0....')

server = smtplib.SMTP(mailserver,587)
server.ehlo()
server.starttls()
server.login('tomkly000@gmail.com','wanghengwolf')
failed = server.sendmail(From,To,text)

server.quit()
if failed:print('Failed recipients ',failed)
else:print('finished.')
