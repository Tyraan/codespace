__author__ = 'Tyraan'
import os,getpass,sys
from urllib.request import urlopen


filename = ''
password = getpass.getpass('Pswd?')


remoteaddr = sys.argv[1]
print('downloading ',remoteaddr)


remotefile = urlopen(remoteaddr)
localfile = open(filename,'wb')
localfile.write(remotefile.read())
localfile.close()

remotefile.close()
