import requests,os
from zhihu_oauth import ZhihuClient
from bs4 import BeautifulSoup
from config import zhihu_email,zhihu_passwd,zhihu_token

questid = 59942156
dirname = r'E:\zhihu_gays'

fails = []
pics = 0
def get_and_save(url, filename, dirname):
    ext = url.split('.')[-1]
    fullpahtname = os.path.join(dirname,filename+'.'+ext)
    img = requests.get(url)

    if img.status_code == 200:
        with open(fullpahtname,'wb') as f:
            f.write(img.content)
    else:
        raise BaseException()



if not os.path.exists(dirname):
    os.mkdir(dirname)

client = ZhihuClient()
#login
if os.path.isfile(zhihu_token):
    client.load_token(zhihu_token)
else:
    client.login_in_terminal()
    client.save_token(zhihu_token)


question = client.question(questid)
anynomous = 0
for answer in question.answers:
    soup = BeautifulSoup(answer.content, 'html5lib')
    imgs = soup.find_all('img')
    name = answer.author.name if answer.author.name != '匿名用户' else  '匿名用户' + str(answer.id)
    print('the answer of ', name, 'include ',len(imgs) ,' images')
    for imgNum in range(len(imgs)):
        if imgs[imgNum].has_attr('data-original'):
            url = imgs[imgNum].attrs['data-original']
            filename = name + str(imgNum)
            try:
                get_and_save(url, filename, dirname)
                pics += 1
            except:
                fails.append(url)
        else:
            if imgs[imgNum].has_attr('src'):
                fails.append(imgs[imgNum].attrs['src'])
            else:
                fails.append(imgs[imgNum])

print('picture download finished , %04d success , %04d failed'%(pics, len(fails)))
