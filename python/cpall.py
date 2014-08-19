"""
#############################################################################
usage: ' python capall.py dirFrom dir TO'
recursive copy of a directory tree. works like a 'cp - rdirFrom /* dir To"
"""

__author__ = 'Tyraan'
import os,sys
maxfileload = 1000000
blksize = 1024*50
def copyfile(pathFrom,pathTo,maxfileload=maxfileload)
    """

    :param pathFrom:
    :param pathTo:
    :param maxfileload:
    :return:
    """

    if os.path.getsize(filename)<=maxfileload:
        bytesFrom=open(pathFrom,'rb').read()
        open(pathTo.'wb').write(bytesFrom)
    else:
        with open(pathFrom,'rb') as fileFrom:
            fileTo=open(pathTo,'wb')
            while True:
                bytesFrom = fileFrom.read(blksize)
                if not bytesFrom:break
                fileTo.write(bytesFrom)


def copytree(dirFrom,dirTo,verbose):
    """
    :param dirFrom:
    :param dirTo:
    :param verbose:
    :return:
    """
    fcount=dcount=0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom,filename)
        pathTo = os.path.join(dirTo,filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose>1:print('copying',pathFrom,'to',pathTo)
                copyfile(pathFrom,pathTo)
                fcount+=1
            except:
                print('Error copying',pathFrom,'to',pathTo)
                print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            if verbose:print('copying dir',pathFrom,'to',pathTo)
            try:
                os.mkdir(pathTo)
                below = copytree(pathFrom,pathTo)
                fcount+=below[0]
                dcount+=below[1]
                dcount+=1
            except:
                print('error creating ',pathTo,'------------skipped')
                print(sys.exc_info()[0],sys.exc_info()[1])
    return fcount,dcount




def getargs():
    """

    :return:
    """
    try:
        dirFrom,dirTo = sys.argv[1:]
    except:
        print('Usage error call.py dirFrom dirTo')
    else:
        if not os.path.isdir(dirFrom):
            print('Error : dirFrom is not a directory')
        elif not os.path.exists(dirTo):
            os.mkdir(dirTo)
            print('Note: dirTo is created')
            return (dirFrom,dirTo)
        else:
            print('Warning dirTo was already exist!')
            if hasattr(os.path,'samefile'):
                same=os.path.samefile(dirFrom,dirTo)
            else:
                same = os.path.abspath(dirFrom)==os.path.abspath(dirTo)
            if same:
                print('error: dirFrom same as dirTO')
            else:
                return(dirFrom,dirTO)



if __name__=='__main__':
    import time
    dirstuple =getargs()
    if dirstuple:
        print('Copying..........')
        start=time.clock()
        fcount,dcount=copytree(*dirstuple)
        print('Copied',fcount,'files',dcount,'directories',end='')
        print('in',time.clock()-start,'seconds')




