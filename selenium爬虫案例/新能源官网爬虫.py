from selenium import webdriver
#from bs4 import BeautifulSoup
#import requests
import time
#import re
driver = webdriver.Chrome()
driver.implicitly_wait(10)
f = open('公司.txt','a',encoding='utf-8')
def get_data(url):

    #res = requests.get(url)
    #soup = BeautifulSoup(res.text,'html.parser')
    driver.get(url)
    time.sleep(1)
    companys = driver.find_elements_by_xpath('/html/body/table[4]/tbody/tr/td[1]/table')
    for item in companys[6:-1]:
        print('请求数据成功！')
        f.write(item.text)
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
    next_page = driver.find_element_by_xpath('/html/body/table[4]/tbody/tr/td[1]/table[27]/tbody/tr/td[2]/a[1]').click()
    time.sleep(1)
if __name__ == '__main__':
    urls = ['http://www.china-nengyuan.com/company/company_list.php?gopage={}&keyword=%E5%8F%B8'.format(str(i)) for i in range(1420,1438)]
    for url in urls:
        get_data(url)
f.close()





