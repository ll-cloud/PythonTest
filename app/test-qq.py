# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["automationName"] = "Appium"
caps["deviceName"] = "127.0.0.1:7555"
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = True

# 连接appium服务器
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el1.clear()
el1.send_keys("70536024")
el2 = driver.find_element_by_accessibility_id("密码 安全")
el2.clear()
el2.send_keys("ly196116")
el3 = driver.find_element_by_accessibility_id("登 录")
el3.click()
el5 = driver.find_element_by_id("com.tencent.mobileqq:id/e3u")
el5.click()
el6 = driver.find_element_by_accessibility_id("设置")
el6.click()
el7 = driver.find_element_by_accessibility_id("帐号管理")
el7.click()
el8 = driver.find_element_by_accessibility_id("退出QQ")
el8.click()
el9 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
el9.click()

driver.quit()