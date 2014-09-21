__author__ = 'Tyraan'
listonly = False
showhdrs = ['From','Subject','Date','Newsgroups','Lines']

nntpconfig  = ()

try:
    import sys
    servername,groupname,showcount = sys.argv[1:] or nntpconfig
    showcount = int(showcount)

except:
    servername = nntpconfig.servername
    groupname = 'comp.lang.python'
    showcount = 10



print ('connect to ', servername ,'for ' ,groupname)
from nntplib import NNTP
connection = NNTP(servername)
(reply,count,first,last,name) =connection.group(groupname)

print('%s has articles %s -%s'%(name,count, first,last))

fetchfrom = str(int(last)-(showcount-1))

(reply ,subjects) = connection.xhdr('subject',(fetchfrom+'-'+last))

for (id, subj) in subjects:
    print ('Article%s[%s]'%(id, subj))
    if not listonly and input('=> Dsilay? ') in ['y',"Y"]:
        reply, num,tid,list = connection.head(id)
        for line in list:
            for prefix in showhdrs:
                if line[:len(prefix)]==prefix:
                    print(line[:80])
                    break
        if input('=> show body ?') in ['y','Y']:
            reply,num, tid, list = connection.body(id)

            for line in list:
                print (line[:80])
    print()
print(connection.quit())



