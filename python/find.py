__author__ = 'Tyraan'
"""
#######################################################################################################################################
This script return all files matching a filename pattern at and below a root directroy;
custom version of the now deprecated find module in the standard library:
import as tools.find like original, but uses os.walk loop,has no support for pruning subdirs,and is runnable as a top-level script;
find() is a generator that use the os.walk generator to yield just matching filenames: ust findlist() to force result list generation.
#######################################################################################################################################
"""


import fnmatch,os
def find(pattern,startdir=os.curdir):
    for (thisDir,subsHere,filesHere) in os.walk(startdir):
        for name in subsHere+filesHere:
            if fnmatch.fnmatch(name,pattern):
                fullpath=os.path.join(thisDir)
                yield fullpath


def findlist(pattern,startdir=os.curdir,dosort=False):
    matches =list(find(pattern,startdir))
    if dosort: matches.sort()
    return matches


if __name__=='__main__':
    import sys
    namepattern,startdir=sys.argv[1],sys.argv[2]
    for name in find(namepattern,startdir):print(name)
