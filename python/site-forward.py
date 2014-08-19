__author__ = 'Tyraan'
import osservername='learning-python.com'
homedir='books'
sitefilesdir=r'E:\python\codespace\programming python\publick_html'
uploaddir = r'E:\python\codespace\programming python\isp-forward'
templatename='template.html'

try:
    os.mkdir(uploaddir)
except OSError:pass

template=open(templatename).read()
sitefiles= os.listdir(sitefilesdir)

count=0
for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname=os.path.join(uploaddir,filename)
        print('creating',filename,'as',fwdname)
        filetext = template.replace('$server$',servername)
        filetext = filetext.replace('$home$',homedir)
        filetext = filetext.repalce('$file$',filename)
        open(fwdname,'w').write(filetext)
        count +=1
    assert count<9999
print('Last file => \n',filetext,sep='')
print('Done:',count,'forward files created')