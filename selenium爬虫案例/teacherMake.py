from selenium import webdriver
import time
import csv

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://jczy.ccgp.gov.cn/gs1/gs1agentreg/pubListIndex.regx')
f=open('teacherMake.csv','a')
def run(i):
    bt = driver.find_element_by_xpath('html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[7]/input')
    bt.send_keys(Keys.CONTROL,'a')
    bt.send_keys(Keys.BACK_SPACE)
    bt.send_keys(str(i))
    bt.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        companys = driver.find_elements_by_xpath('html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr')
        #print(companys)
        for company in companys:
            agent = company.find_element_by_css_selector('td[field="agentNm"]')
            agent = agent.text
            contact_people = company.find_element_by_css_selector('td[field="contactNm"]')
            contact_people = contact_people.text
            tel = company.find_element_by_css_selector('td[field="corpTel"]')
            tel = tel.text
            add = company.find_element_by_css_selector('td[field="regAddr"]')
            add = add.text
            #print(agent,contact_people,tel,add)
            f.write(','.join([agent,contact_people,tel,add])+'\n')
    except:
        companys = driver.find_elements_by_xpath('html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr')
        #print(companys)
        for company in companys:
            agent = company.find_element_by_css_selector('td[field="agentNm"]')
            agent = agent.text
            contact_people = company.find_element_by_css_selector('td[field="contactNm"]')
            contact_people = contact_people.text
            tel = company.find_element_by_css_selector('td[field="corpTel"]')
            tel = tel.text
            add = company.find_element_by_css_selector('td[field="regAddr"]')
            add = add.text
            #print(agent,contact_people,tel,add)
            f.write(','.join([agent,contact_people,tel,add])+'\n')
        #print("数据存储成功！")
##    btn = driver.find_elements_by_xpath('//*[@id="undefined"]/span/span/span')[2]
##    btn.click()
if __name__ == "__main__":
    for i in range(1,729):
               
        run(i)
        print(i)
driver.quit()

f.close()
driver.quit()
