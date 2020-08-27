from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://jczy.ccgp.gov.cn/gs1/gs1agentreg/pubListIndex.regx')


fp = open('doubanbook.csv', 'wt', newline='', encoding='utf-8')





def run():
    #driver.get('http://jczy.ccgp.gov.cn/gs1/gs1agentreg/pubListIndex.regx')

    companys = driver.find_elements_by_xpath('/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/table/tbody/tr')

    for company in companys:
        agent = company.find_element_by_css_selector('td[field="agentNm"]')
        agent = agent.text
        contact_people = company.find_element_by_css_selector('td[field="contactNm"]')
        contact_people = contact_people.text
        tel = company.find_element_by_css_selector('td[field="corpTel"]')
        tel = tel.text
        add = company.find_element_by_css_selector('td[field="regAddr"]')
        add = add.text
        print(agent,contact_people,tel,add)
        writer = csv.writer(fp)
        writer.writerow((agent,contact_people,tel,add))

    btn = driver.find_element_by_class_name('.l-btn-empty pagination-next')
    btn.click()


if __name__ == "__main__":
    for i in range(1,729):
        run()

fp.close()
driver.quit()





