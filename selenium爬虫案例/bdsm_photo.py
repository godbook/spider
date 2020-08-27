from selenium import webdriver
import requests
driver = webdriver.Chrome()
driver.implicitly_wait(10)
import time

book = []


def get_img(url):
    driver.get(url)
    time.sleep(1)
    encoding = 'utf-8'
    imgs = driver.find_elements_by_tag_name('img')
    for img in imgs:
        x=img.get_attribute("src")
        book.append(x)
    num = 200    
    for each in book:
        each = str(each)
        res = requests.get(each)
        print('请求图片成功了')
        f = open(f'第{num}章.jpg','wb')
        f.write(res.content)
        f.close()
        num += 1

if __name__ == '__main__':
    urls = ['https://femaledominationworld.com/page/{}'.format(str(i)) for i in range(1,1700)]
    for url in urls:
        get_img(url)
