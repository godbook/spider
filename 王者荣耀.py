import requests
from bs4 import BeautifulSoup
import re
import time
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'femaledominationworld.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode':' navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
book = []
def get_data(url):  
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        book.append("http:"+img.get("src"))
    num = 0
    for item in book:
        item = str(item)
        respon = requests.get(item)
        print("请求图片成功！")
        with open(f"第{num}张.jpg","wb") as f:
            f.write(respon.content)
            f.close()
            num += 1
if __name__ == '__main__':
    urls = ['https://femaledominationworld.com/page/{}'.format(str(i)) for i in range(1,1707)]
    for url in urls:
        get_data(url)
        

