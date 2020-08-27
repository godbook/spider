
from selenium import webdriver
from PIL import Image
from selenium.webdriver import ActionChains
from time import sleep

def shot_img(driver):
    sleep(2)
    # 截取整个浏览器的图
    driver.save_screenshot("./page.png")
    # 加载图片
    img = Image.open("./page.png")
    # img.show()
    # 从整个浏览器区域中截取出验证码区域
    loc = driver.find_element_by_xpath('//*[@id="captcha_div"]/div/div[1]/div/div[1]/img[1]').location # 提取验证码区域的位置(距x轴和距y轴的距离)
    size = driver.find_element_by_xpath('//*[@id="captcha_div"]/div/div[2]/div[2]').size # 提取验证码区域的大小（宽和高）
    # 根据loc和size来计算验证码区域的截取范围
    top = loc["y"]
    bottom = loc["y"] + size["height"]
    left = loc["x"]
    right = loc["x"] + size["width"]
    # 根据截取范围将验证码区域的图片截取出来(后面的系数根据自己电脑配置自行调节)
    code_img = img.crop((left*2,top/2,right*2,bottom*1.2))
    # code_img.show()
    return code_img

# 封装一个函数，用于根据两张图片的像素差异来计算滑动距离
def get_distance(img1,img2):
    for i in range(50,img1.size[0]):
        for j in range(0,img1.size[1]):
            # 获取每一个像素点的rgb值
            rgb1 = img1.load()[i,j]
            rgb2 = img2.load()[i,j]
            # 计算两个图片的rgb差异
            r = abs(rgb1[0] - rgb2[0])
            g = abs(rgb1[1] - rgb2[1])
            b = abs(rgb1[2] - rgb2[2])
            # 判断差异
            if r>60 and g>60 and b>60:
                return i/2 - 6


# 封装一个函数，用于提供模拟匀加速运动的轨迹
def tracks(distance):
    # 拖动的时候多拖出去20
    distance += 20
    v = 0
    t = 0.2
    # 定义一个中间位置，以前匀加速，以后匀减速
    mid = distance*3/5
    # 定义一个变量用于记录当前位置
    current = 0
    # 定义一个变量用于存放每一段的轨迹
    farwords = []
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        s = v*t + 1/2*a*t**2
        v = a*t + v
        current += s
        # 将每一段的位移s加入轨迹中
        farwords.append(round(s))
    # 返回一个字典，里面存放前向和反向轨迹
    return {"farwords":farwords,"backs":[-3,-3,-3,-2,-2,2,-2,-2,-3,-1,-1]}
# 封装一个函数，用于破解滑动验证码
def crack_code(driver):
    # 1、计算滑动距离
    # 1）截取带缺口的图
    img1 = shot_img(driver)
    # 2）去掉缺口
    # 用js语句来去掉缺口
    js = "document.querySelector('.yidun_bg-img').style.zIndex=10;document.querySelector('.yidun_bg-img').style.display='block';document.querySelector('.yidun_jigsaw').style.display='block';"
    driver.execute_script(js)

    # 3）截取不带缺口的图
    img2 = shot_img(driver)

    # 4）把去掉的缺口补回来
    js = "document.querySelector('.yidun_bg-img').style.zIndex=10;document.querySelector('.yidun_bg-img').style.display='block';document.querySelector('.yidun_jigsaw').style.display='none';"
    driver.execute_script(js)

    # 5) 根据两张图片的缺口处的像素差异，来求出存在差异的第一个像素的x轴坐标，即为滑动距离
    distance = get_distance(img1,img2)
    print(distance)
    # 2、模拟人类的动作来滑动
    btn = driver.find_element_by_class_name("geetest_slider_button")
    # 1)按住滑块按钮
    ActionChains(driver).click_and_hold(btn).perform()
    sleep(0.5)
    # 2）按照距离来拖动
    # ActionChains(driver).move_by_offset(xoffset=distance,yoffset=0).perform() # 拖动的时候要尽量慢一些更像人类动作
    # 获取轨迹
    track_dict = tracks(distance)
    # 前向移动
    for track in track_dict["farwords"]:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    sleep(0.5)
    # 反向移动
    for track in track_dict["backs"]:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    sleep(0.5)
    # 3）松开滑块按钮
    ActionChains(driver).release().perform()

def login_blogs(url):
    # 创建一个driver对象
    driver = webdriver.Chrome(r'C:\Users\admin\Desktop\chromedriver.exe')
    driver.implicitly_wait(10)
    try:
        driver.get(url)
        page_input = driver.find_element_by_xpath('//*[@id="query_querydata_input"]').send_keys('中国\n')
        item_1 = driver.find_element_by_xpath('//*[@id="query_result"]/table/tbody/tr[2]/td[7]/a').click()
        for handle in driver.window_handles:
            
        # 先切换到该窗口
            driver.switch_to.window(handle)
        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
            if '访问行为验证' in driver.title:  
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
                break
        # 破解滑动验证码
        crack_code(driver)
    finally:
        driver.close()


if __name__ == '__main__':
    url = "http://app.miit-eidc.org.cn/miitxxgk/gonggao/xxgk/index"
    login_blogs(url)
