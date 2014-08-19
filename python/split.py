import os

kilobytes=1024
megabytes=kilobytes *1000
chunksize=int(1.4*megabytes)
def split(fromfile,todir,chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))

    partnum=0
    input = open(fromfile,'rb')
    while True:
        chunk=input.read(chunksize)
        if not chunk:break
        partnum+=1
        filename=os.path.join(todir,('part%04d'%partnum))
        fileobj=open(filename,'wb')
        fileobj.write(chunk)
        fileobj.close()
    input.close()
    assert partnum<=9999
    return partnum

