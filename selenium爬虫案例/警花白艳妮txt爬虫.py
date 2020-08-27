from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10)

f = open('白艳妮.txt','a')

def get_data(url):
    driver.get(url)
    content = driver.find_element_by_xpath('//*[@id="contents"]')
    f.write(content.text)




if __name__ == '__main__':

    urls = ['http://www.2shu.net/dushu/0/975/99{}.html'.format(str(i)) for i in range(169,229)]
    for url in urls:
        get_data(url)
