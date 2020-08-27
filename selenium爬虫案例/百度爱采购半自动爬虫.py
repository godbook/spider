from selenium import webdriver
import time
import csv
import re

browser = webdriver.Chrome()

url = "https://b2b.baidu.com/c?q=%E6%B5%B7%E6%B0%B4%E6%B7%A1%E5%8C%96&from=search"

browser.implicitly_wait(5)

xx='class="c-c-title c-link">(.*?)</span>'
yy=r'注册地址：</label><span data-v-2e0d3bb2="" title="(.*?)"'
if __name__ == "__main__":
    
    browser.get(url)

    for i in range(2):
        s= browser.page_source
        companys=re.findall(xx,s)
        address=re.findall(yy,s)
        for q,j in zip(companys,address):
            print("数据请求成功！")
            f = open("海水淡化.csv","a",encoding="utf-8",newline="")
            csv_writer = csv.writer(f)
            csv_writer.writerow([q,j])
        if i<2:
            a = browser.find_element_by_link_text("下一页")
            
            a.click()
            time.sleep(2)
f.close()
browser.quit()




