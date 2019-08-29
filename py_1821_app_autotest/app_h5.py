# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

from appium import webdriver
# from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# 1、启动参数

desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "8.1.0"  # 平台版本
desired_caps["deviceName"] = "Android Emulator"  # 设备名称
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.WelcomeActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态
desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("乐付")')
WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
# 获取当前所有的contexts
cons = driver.contexts
print(cons)

driver.find_element(*loc).click()

# 等待webview元素出现
loc = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
time.sleep(2)

# 获取当前所有的contexts
cons = driver.contexts
print(cons)

# 切换到 webview --- 切换到html页面
driver.switch_to.context(cons[1])
time.sleep(2)
print("当前的context: ", driver.current_context)

print("=======================进入web自动化======================")
# 怎么得到html页面，并进行元素定位？？
# 1、 工具 - uc devtools
# 2、 chrome://inspect
# 3、 driver.page_source得到html页面。保存在一个文件中用chrome访问。
# 4、 直接找开发获取内嵌的html

# 注意chromedriver的版本 要与  安卓 系统的webview版本匹配
# 可以通过desired_caps["chromedriverExecutable"] 来指定 chromedriver的路径 。

# //button[text()="立即购买"]
loc = (MobileBy.XPATH, '//button[text()="立即购买"]')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 步骤： 识别、开启调试模式、得到所有上下文、切换到webview、定位元素并操作(chromedriver的版本匹配)
