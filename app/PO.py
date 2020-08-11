# coding=utf-8
from appium import webdriver


class QQAuto:
    def __init__(self):
        """
        启动Appuim服务
        :return:
        """
        caps = {}
        caps["automationName"] = "Appium"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["appPackage"] = "com.tencent.mobileqq"
        caps["appActivity"] = ".activity.SplashActivity"
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    def login(self):
        """
        登录模块
        :return:
        """
        el1 = self.driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
        el1.send_keys("70536024")
        el2 = self.driver.find_element_by_accessibility_id("密码 安全")
        el2.clear()
        el2.send_keys("ly196116")
        el3 = self.driver.find_element_by_accessibility_id("登 录")
        el3.click()

    def loginout(self):
        """
        登出模块
        :return:
        """
        # 增加点击消息界面
        # el1 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabWidget/android.widget.RelativeLayout")
        # el1.click()
        el6 = self.driver.find_element_by_accessibility_id("帐户及设置")
        el6.click()
        el7 = self.driver.find_element_by_id("com.tencent.mobileqq:id/gso")
        el7.click()
        el8 = self.driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
        el8.click()
        el9 = self.driver.find_element_by_accessibility_id("退出当前帐号按钮")
        el9.click()
        el10 = self.driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
        el10.click()

    def quit(self):
        self.driver.quit()
