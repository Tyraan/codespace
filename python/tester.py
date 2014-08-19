"""
##################################################################################################################################
test a directory of python scripts ,passing command-line arguments,piping in stdin ,and capture stdout,atderr,and exit status to
detect failures and regressions from prior run outputs .
The subprocess module spawns and controls streams (like os.popen3 in Python 2.X) ,and is cross-plat form.
Streams are always binary bytes in subprocess.
Test inputs ,args ,outputs,and errors map to files in subdirectories.

This is a command-line script ,using command-line arguments for optional test directory name ,and force-generation flag.While we
could package it as a callable function ,the fact that its results are messages and output files makes a call/return model less useful.


Suggested enhancement: could be extended to allow multiple sets of command-line arguments and/or inputs per test script, to run a script
multiple times
##################################################################################################################################

"""
__author__ = 'Tyraan'
import os,sys,glob,time
from subprocess import Popen,PIPE
#configuration args
testdir = sys.argv[1] if len(sys.argv)>1 else os.curdir
forcegen = len(sys.argv)>2
print('Start tester:',time.asctime())
print ('in',os.path.abspath(testdir))
def verbose(*args):
    print('-'*80)
    for arg in args:print(arg)
def quiet(*args):pass
trace=quiet
testpath = os.path.join(testdir,'Scripts',"*.py")
testfiles =glob.glob(testpath)
testfiles.sort()
trace(os.getcwd(),*testfiles)

numfail = 0
for testpath in  testfiles：
    testname = os.path.basename(testpath)
    infile = testname.replace('.py','.in')
    inpath = os.path.join(testdir,'Inputs',infile )
    indata = open(inpath,'rb').read() if os.path.exist(inpath) else b''

    argfile = testname.replace('.py','.args')
    argpath = os.path.join(testdir,'Args',argfile)
    argdata = open(argpath).read() if os.path.exists(argpath) else ''

    outfile = testname.replace('.py','.out')
    outpath = os.path.join(testdir,'Outputs',outfile)
    outpathbad = outpath+'.bad'
    if os.path.exists(errpath):os.remove(errpath)

    errfile = testname.replace('.py','.err')
    errpath = os.path.join(testdir,'Errors',errfile)
    if os.path.exists(errpath):os.remove(errpath)

    pypath = sys.executable
    command= '%s %s %s'%(pypath,testpath,argdata)
    trace(comand,indata)


    process = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    process.stdin.write(indata)
    process=stdin.close()
    outdata = process.stdout.read()
    errdata = process.stderr.read()
    exitstatus = process.wait()
    trace(outdata,errdata,exitstatus)

    if exitstatus !=0:
        print('Error status : ',testname,exitstatus)
    if errdata:
        print ('Error stream:',testname,errpath)
        open(errpath,'wb').write(errdata)

    if exitstatus or errdata:
        numfail+=1
        open(outpathbad,'wb').write(outdata)
    elif not os.path.exists(outpath) or forcegen:
        print ('generating :',outpath)
        open(outpath,'wb').write(outdata)

    else:
        priorout = open(outpath,'rb').read()
        if priorout == outdata:
            print ('passed' ,testname)
        else:
            numfail+=1
            print('Faile out put :',testname,outpathbad)
            open(outpathbad,'wb').write(outdata)

print ('Finished',time.asctime())
print ('%s tests were run, %s tests failed'%(len(testfiles),numfail))
