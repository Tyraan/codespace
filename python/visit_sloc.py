__author__ = 'Tyraan'
import sys,pprint,os
from visitor import FileVisitor
class LinesByType(FileVisitor):
    srcExts=[]

    def __init__(self,trace=1):
        FileVisitor.__init__(self,trace=trace)
        self.srcLines=self.srcFiles=0
        self.extSums={ext:dict(files=0,lines=0) for ext in self.srcExts }

    def visitsource(self,fpath,ext):
        if self.trace > 0:print(os.path.basename(fpath))
        lines = len(open(fpath,'rb').readlines())
        self.srcFiles += 1
        self.srcLines += 1
        self.extSums[ext]['files'] +=1
        self.extSums[ext]['lines'] +=1

    def visitfile(self,filepath):
        FileVisitor.visitfile(self,filepath)
        for ext in self.srcExts:
            if filepath.endswith(ext):
                self.visitsource(filepath,ext)
                break


class PyLines(LinesByType):
    srcExts=['.py','.pyw']

class SourceLines(LinesByType):
    srcExts=['.py','.pyw','.cgi','.html','.c','.cxx','.h','.i']





if __name__=='__main__':
    walker =SourceLines()
    walker.run(sys.argv[1])
    print('Visited %d files and %d dirs'%(walker.fcount,walker.dcount))
    print ('_'*80)
    print ('Source file => %d,lines =>%d'%(walker.srcFiles,walker.srcLines))
    print ('By Types:')
    pprint.pprint(walker.extSums)

    print('\n Check sums:',end = '')
    print(sum(x['lines'] for x in walker.extSums.values()),end='')
    print(sum(x['files'] for x in walker.extSums.values()))

    print ('\n Python only walk:')
    walker = PyLines(trace=0)
    walker.run(sys.argv[1])
    pprint.pprint(walker.extSums)


