
__author__ = 'Tyraan'
from getpass import getpass


from ftplib import FTP
from os.path import exists

def getfile(file,site,dir,user=(),*,verbose = True,refetch = False):
    if exists(file) and not refetch:
        if verbose:print('file has been fetched.')
    else:
        if verbose:print('Downloading file ',file)
        local = open (file,'wb')
        try :
            remote = FTP(site)
            remote.login(*user)
            remote.cwd(dir)
            remote.retrbinary('RETR'+file,local.write,1024)
            remote.quit()
        finally:
            local.close()
        if verbose:
            print('Download done.')






filename = 'monkeys.jpg'
getfile(file = filename,
        site = 'ftp.rmi.net',
        dir  = '.',
        user = ('lutz',getpass('Pswd?')),
        refetch = True)




