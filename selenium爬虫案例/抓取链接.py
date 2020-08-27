
from bs4 import BeautifulSoup
import requests
import re
import time

headers = {
    'Accept': 'texthtml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1594716614,1594772644,1594805063,1594869686; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1594870923',
    'Host': 'www.ccgp.gov.cn',
    'Referer': 'http://www.ccgp.gov.cn/zcfg/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
f = open('links.csv','a')

def get_link(url):  
    html = requests.get(url,headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,"html.parser")

    links = re.findall('href="(\..*?)"',str(soup))
    for link in links:
        link = link[1:]
        print('http://www.ccgp.gov.cn/zcfg/dffg'+link)
        f.write('http://www.ccgp.gov.cn/zcfg/dffg'+link+'\n')
        


       
         
if __name__ == '__main__':
    urls = ['http://www.ccgp.gov.cn/zcfg/dffg/index_{}.htm'.format(int(i)) for i in range(1,17)]
    for url in urls:
        get_link(url)
        
        
f.close()



