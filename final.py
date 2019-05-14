#图像处理标准库
from PIL import Image
#web测试
from selenium import webdriver
#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
#等待时间 产生随机数
import time,random


#打开页面至屏幕最大尺寸
driver = webdriver.Chrome()
driver.get('https://passport.douyu.com/iframe/loginNew')
driver.maximize_window()
#获取输入手机号码的表单
input1 = driver.find_element_by_name('username')
# 输入注册号码
input1.send_keys("1")
input2 = driver.find_element_by_name('password')
# 输入注册号码
input2.send_keys("2")
time.sleep(0.2)
#获取打开滑块验证码页面的元素
getcheck = driver.find_element_by_class_name("loginbox-sbt btn-sub")
#getcheck=driver.find_element_by_id('getDynamicPwd')
#点击进入滑块验证码页面
getcheck.click()
